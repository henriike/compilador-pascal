from AbstractVisitor import AbstractVisitor
import SymbolTable as st
from SymbolTable import *

from Visitor import Visitor
import SintaxeAbstrata as sa



def coercion(type1, type2):
    if (type1 in st.Number and type2 in st.Number):
        if (type1 == st.REAL or type2 == st.REAL):
            return st.REAL
        else:
            return st.INTEGER
    else:
        return None



# Em uma operação entre integer e real utilizando o div é retornado integer
def coercionDDivExp(exp1, exp2):
    if (exp1 in st.Number and exp2 in st.Number):
        return st.INTEGER
    else:
        return None



# Verifica se o tipo de exp1 é igual ao tipo de exp2
def validaTipo(exp1, exp2):
    if (exp1 in st.Number and exp2 in st.Number):
        return st.BOOL
    elif (exp1 == exp2):
        return st.BOOL
    else:
        return None


# Expressão da esquerda e expressão da direita precisam ser numéricas
def validaExpressaoNumerica(exp1, exp2):
    if (exp1 in st.Number and exp2 in st.Number):
        return st.BOOL
    else:
        return None


# Expressão da direita precisa ser um número
def validaUnaria(exp1):
    if (exp1 in st.Number):
        if (exp1 == st.REAL):
            return st.REAL
        else:
            return st.INTEGER
    else:
        return None


# Expressão da esquerda e expressão da direita precisam ser booleanas
def validaExpressaoBooleana(exp1, exp2):
    if (exp1 == st.BOOL and exp2 == st.BOOL):
        print('entrei')
        return st.BOOL
    else:
        return None



# Estamos traduzindo os parâmetros para um dicionário, porque originalmente estão como string
def translateToDicParams(pStr):
    dic = {}
    for p in pStr.split(';'):

        l = p.split(':')

        if ',' in l[0]:
            for v in l[0].split(','):
                dic[v.strip()] = l[1].strip()
        elif len(l) == 2:
            dic[l[0].strip()] = l[1].strip()

    return dic



class SemanticVisitor:

    def __init__(self):
        self.printer = Visitor()
        st.beginScope('main')


    def visitPProgram(self, pProgram):
        if (pProgram.block != None):
            pProgram.block.accept(self)


    def visitBBlock(self, bBlock):
        if bBlock.const_dec != None:
            bBlock.const_dec.accept(self)
        if bBlock.var_dec != None:
            bBlock.var_dec.accept(self)
        if bBlock.subroutine_dec != None:
            for i in bBlock.subroutine_dec:
                i.accept(self)
        if bBlock.compoundStatement_dec != None:
            bBlock.compoundStatement_dec.accept(self)


    def visitCConstDefinition(self, cConstDefinition):
        if cConstDefinition != None:
            for i in cConstDefinition.dicDefinicoes.keys():
                if isinstance(cConstDefinition.dicDefinicoes[i], int):
                    addConst(i, st.INTEGER)
                elif isinstance(cConstDefinition.dicDefinicoes[i], float):
                    addConst(i, st.REAL)
                elif isinstance(cConstDefinition.dicDefinicoes[i], str):
                    addConst(i, st.STRING)




    def visitVVarDeclaration(self, vVarDeclaration):
        if vVarDeclaration != None:
            for i in vVarDeclaration.dicDefinicoes.keys():
                addVar(i, vVarDeclaration.dicDefinicoes[i])



    def visitPProcedureDeclaration(self, pProcedureDeclaration):
        if pProcedureDeclaration != None:
            for key, v in pProcedureDeclaration.dicDefinicoes.items():
                dic = translateToDicParams(v)
                addProcedure(key, dic)



    def visitFFunctionDeclaration(self, fFunctionDeclaration):
        if fFunctionDeclaration != None:
            for key, v in fFunctionDeclaration.dicDefinicoes.items():
                dic = translateToDicParams(key)
                addFunction(fFunctionDeclaration.id, dic, v)



    def visitCCompoundStatementScore(self, cCompoundStatementScore):
        if cCompoundStatementScore != None:
            cCompoundStatementScore.statements.accept(self)



    def visitCCompoundStatementSemicolon(self, cCompoundStatementSemicolon):
        if cCompoundStatementSemicolon != None:
            cCompoundStatementSemicolon.statements.accept(self)



    def visitSSingleStatement(self, sSingleStatement):
        if sSingleStatement != None:
            sSingleStatement.statementt.accept(self)



    def visitCCompoundStatement(self, cCompoundStatement):
        if cCompoundStatement != None:
            cCompoundStatement.statementt.accept(self)
            cCompoundStatement.statementss.accept(self)



    def visitSSingleExprList(self, sSingleExprList):
        sSingleExprList.expr.accept(self)

    def visitCCompoundExprList(self, cCompoundExprList):
        cCompoundExprList.expr1.accept(self)
        cCompoundExprList.expr2.accept(self)




    def visitAAssignStatement(self, aAssignStatement):
        if aAssignStatement != None:
            typeVar = aAssignStatement.exp.accept(self)
            infoBind = st.getBindable(aAssignStatement.id)

            if infoBind != None:
                if infoBind[st.BINDABLE] == st.VARIABLE:
                    if infoBind[st.TYPE] != typeVar:
                        print("[ASSIGN] A expressão ", end='')
                        aAssignStatement.exp.accept(self.printer)
                        print(" possui tipo diferente da variavel", aAssignStatement.id)
                    else:
                        return typeVar
                elif infoBind[st.BINDABLE] == st.CONST:
                    print("O identificador", aAssignStatement.id, "é uma constante, portanto não pode ser modificado")

        return None



    def visitPPlusExp(self, pPlusExp):
        tipoExp1 = pPlusExp.exp1.accept(self)
        tipoExp2 = pPlusExp.exp2.accept(self)

        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            pPlusExp.accept(self.printer)
            print('\n\t[Erro] Soma invalida. A expressao ', end='')
            pPlusExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            pPlusExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2, '\n')
        return c


    def visitMMinusExp(self, mMinusExp):
        tipoExp1 = mMinusExp.exp1.accept(self)
        tipoExp2 = mMinusExp.exp2.accept(self)

        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            mMinusExp.accept(self.printer)
            print('\n\t[Erro] Subtracao invalida. A expressao ', end='')
            mMinusExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            mMinusExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2, '\n')
        return c


    def visitTTimesExp(self, tTimesExp):
        tipoExp1 = tTimesExp.exp1.accept(self)
        tipoExp2 = tTimesExp.exp2.accept(self)

        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            tTimesExp.accept(self.printer)
            print('\n\t[Erro] Multiplicacao invalida. A expressao ', end='')
            tTimesExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            tTimesExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2, '\n')
        return c


    def visitDDivideExp(self, dDivideExp):
        tipoExp1 = dDivideExp.exp1.accept(self)
        tipoExp2 = dDivideExp.exp2.accept(self)

        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            dDivideExp.accept(self.printer)
            print('\n\t[Erro] Divisão invalida. A expressao ', end='')
            dDivideExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            dDivideExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2, '\n')
        return c


    def visitDDivExp(self, dDivExp):
        tipoExp1 = dDivExp.exp1.accept(self)
        tipoExp2 = dDivExp.exp2.accept(self)

        c = coercionDDivExp(tipoExp1, tipoExp2)
        if (c == None):
            dDivExp.accept(self.printer)
            print('\n\t[Erro] Divisão invalida. A expressao ', end='')
            dDivExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            dDivExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2, '\n')
        return c


    def visitMModExp(self, mModExp):
        tipoExp1 = mModExp.exp1.accept(self)
        tipoExp2 = mModExp.exp2.accept(self)

        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            mModExp.accept(self.printer)
            print('\n\t[Erro] Divisão invalida. A expressao ', end='')
            mModExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            mModExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2, '\n')
        return c


    def visitEEqualsExp(self, eEqualsExp):
        tipoExp1 = eEqualsExp.exp1.accept(self)
        tipoExp2 = eEqualsExp.exp2.accept(self)

        c = validaTipo(tipoExp1, tipoExp2)
        if (c == None):
            eEqualsExp.accept(self.printer)
            print('\n\t[Erro] Comparacao invalida. A expressao ', end='')
            eEqualsExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            eEqualsExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2, '\n')
        return c


    def visitDDifferentExp(self, dDifferentExp):
        tipoExp1 = dDifferentExp.exp1.accept(self)
        tipoExp2 = dDifferentExp.exp2.accept(self)

        c = validaTipo(tipoExp1, tipoExp2)
        if (c == None):
            dDifferentExp.accept(self.printer)
            print('\n\t[Erro] Comparacao invalida. A expressao ', end='')
            dDifferentExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            dDifferentExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2, '\n')
        return c


    def visitLLthanExp(self, lLthanExp):
        tipoExp1 = lLthanExp.exp1.accept(self)
        tipoExp2 = lLthanExp.exp2.accept(self)

        c = validaExpressaoNumerica(tipoExp1, tipoExp2)
        if (c == None):
            lLthanExp.accept(self.printer)
            print('\n\t[Erro] Comparacao invalida. A expressao ', end='')
            lLthanExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            lLthanExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2, '\n')
        return c


    def visitGGthanExp(self, gGthanExp):
        tipoExp1 = gGthanExp.exp1.accept(self)
        tipoExp2 = gGthanExp.exp2.accept(self)

        c = validaExpressaoNumerica(tipoExp1, tipoExp2)
        if (c == None):
            gGthanExp.accept(self.printer)
            print('\n\t[Erro] Comparacao invalida. A expressao ', end='')
            gGthanExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            gGthanExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2, '\n')
        return c


    def visitGGequals(self, gGequals):
        tipoExp1 = gGequals.exp1.accept(self)
        tipoExp2 = gGequals.exp2.accept(self)

        c = validaExpressaoNumerica(tipoExp1, tipoExp2)
        if (c == None):
            gGequals.accept(self.printer)
            print('\n\t[Erro] Comparacao invalida. A expressao ', end='')
            gGequals.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            gGequals.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2, '\n')
        return c


    def visitLLequalsExp(self, lLequalsExp):
        tipoExp1 = lLequalsExp.exp1.accept(self)
        tipoExp2 = lLequalsExp.exp2.accept(self)

        c = validaExpressaoNumerica(tipoExp1, tipoExp2)
        if (c == None):
            lLequalsExp.accept(self.printer)
            print('\n\t[Erro] Comparacao invalida. A expressao ', end='')
            lLequalsExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            lLequalsExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2, '\n')
        return c


    def visitAAndExp(self, aAndExp):
        tipoExp1 = aAndExp.exp1.accept(self)
        tipoExp2 = aAndExp.exp2.accept(self)

        c = validaExpressaoBooleana(tipoExp1, tipoExp2)
        if (c == None):
            aAndExp.accept(self.printer)
            print('\n\t[Erro] Comparacao invalida. A expressao ', end='')
            aAndExp.exp1.accept(self.printer)
            print(' eh do tipo', tipoExp1, 'enquanto a expressao ', end='')
            aAndExp.exp2.accept(self.printer)
            print(' eh do tipo', tipoExp2, '\n')
        return c


    def visitUPPlusExp(self, uPPlusExp):
        tipoExp1 = uPPlusExp.exp.accept(self)

        c = validaUnaria(tipoExp1)
        if (c == None):
            print('deu erro')
        return c


    def visitUMMinusExp(self, uMMinusExp):
        tipoExp1 = uMMinusExp.exp.accept(self)

        c = validaUnaria(tipoExp1)
        if (c == None):
            print('deu erro')
        return c


    def visitFFactorString(self, fFactorString):
        fFactorString.type.accept(self)

    def visitFFactorInt(self, fFactorInt):
        return st.INTEGER

    def visitFFactorReal(self, fFactorReal):
        return st.REAL

    def visitFFactorId(self, fFactorId):
        idName = st.getBindable(fFactorId.literal)
        if (idName != None):
            return idName[st.TYPE]
        return None

    def visitFFactorBoolean(self, fFactorBoolean):
        return st.BOOL

    def visitFFactorNot(self, fFactorNot):
        fFactorNot.type.accept(self)