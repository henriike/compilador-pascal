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



    #Construímos a partir daqui

    def visitAAssignStatement(self, aAssignStatement):
        if aAssignStatement != None:
            typeVar = aAssignStatement.exp.accept(self)
            infoBind = st.getBindable(aAssignStatement.id)

            if infoBind != None:
                if infoBind[st.BINDABLE] == st.VARIABLE:
                    if infoBind[st.TYPE] != typeVar:
                        print("A expressão ", end='')
                        aAssignStatement.exp.accept(self.printer)
                        print(" possui tipo diferente do identificador", aAssignStatement.id)
                    else:
                        return typeVar
                elif infoBind[st.BINDABLE] == st.CONST:
                    print("O identificador ", aAssignStatement.id, "é uma constante")

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




    def visitSSingleExprList(self, sSingleExprList):
        sSingleExprList.expr.accept(self)

    def visitCCompoundExprList(self, cCompoundExprList):
        cCompoundExprList.expr1.accept(self)
        cCompoundExprList.expr2.accept(self)





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