import SymbolTable as st
from SymbolTable import *

from AbstractVisitor import AbstractVisitor
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


# Expressão da esquerda e expressão da direita precisam ser booleanas
def validaExpressaoBooleana(exp1, exp2):
    if (exp1 == st.BOOL and exp2 == st.BOOL):
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



class SemanticVisitor(AbstractVisitor):

    def __init__(self):
        self.printer = Visitor()
        st.beginScope('main')

#---------------------------------------------------------------------------------------

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


#---------------------------------------------------------------------------------------


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

#---------------------------------------------------------------------------------------

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

#---------------------------------------------------------------------------------------


    def visitCCompoundStatementScore(self, cCompoundStatementScore):
        if cCompoundStatementScore != None:
            cCompoundStatementScore.statements.accept(self)


    def visitCCompoundStatementSemicolon(self, cCompoundStatementSemicolon):
        if cCompoundStatementSemicolon != None:
            cCompoundStatementSemicolon.statements.accept(self)

#---------------------------------------------------------------------------------------

    def visitSSingleStatement(self, sSingleStatement):
        if sSingleStatement != None:
            sSingleStatement.statementt.accept(self)



    def visitCCompoundStatement(self, cCompoundStatement):
        if cCompoundStatement != None:
            cCompoundStatement.statementt.accept(self)
            cCompoundStatement.statementss.accept(self)

#---------------------------------------------------------------------------------------

    def visitSSingleExprList(self, sSingleExprList):
        return [sSingleExprList.expr.accept(self)]

    def visitCCompoundExprList(self, cCompoundExprList):
        return [cCompoundExprList.expr1.accept(self)] + cCompoundExprList.expr2.accept(self)

#---------------------------------------------------------------------------------------

    def visitAAssignStatement(self, aAssignStatement):
        if aAssignStatement != None:
            typeVar = aAssignStatement.exp.accept(self)
            infoBind = st.getBindable(aAssignStatement.id)

            if infoBind != None:
                if infoBind[st.BINDABLE] == st.VARIABLE:

                    if infoBind[st.TYPE] != st.REAL and infoBind[st.TYPE] != typeVar:
                        aAssignStatement.exp.accept(self.printer)
                        print("\n\t[ASSIGN] A expressão ", end='')
                        aAssignStatement.exp.accept(self.printer)
                        print(" é do tipo", typeVar, "e possui tipo diferente da variável", aAssignStatement.id, "que é do tipo", infoBind[st.TYPE], end= ".\n\n")


                    elif not(typeVar in st.Number) and infoBind[st.TYPE] == st.REAL:
                        aAssignStatement.exp.accept(self.printer)
                        print("\n\t[ASSIGN] A expressão ", end='')
                        aAssignStatement.exp.accept(self.printer)
                        print(" é do tipo", typeVar, "e possui tipo diferente da variável", aAssignStatement.id, "que é do tipo", infoBind[st.TYPE], end=".\n\n")

                    else:
                        return typeVar

                elif infoBind[st.BINDABLE] == st.CONST:
                    aAssignStatement.exp.accept((self.printer))
                    print("\n\t[ASSIGN] O identificador", aAssignStatement.id, "é uma constante, portanto não pode ser modificado.", end=".\n\n")

        return None

#---------------------------------------------------------------------------------------

    def visitPProcedureFFunctionCallStatement(self, pProcedureFFunctionCallStatement):

        # Captura o ID
        bindable = st.getBindable(pProcedureFFunctionCallStatement.id)


        # Caso seja Função
        if (bindable != None and bindable[st.BINDABLE] == st.FUNCTION):
            typeParams = pProcedureFFunctionCallStatement.exprList.accept(self)
            pProcedureFFunctionCallStatement.exprList.accept(self.printer)

            if (list(bindable[st.PARAMS].values()) == typeParams):
                return bindable[st.TYPE]

            pProcedureFFunctionCallStatement.accept(self.printer)
            print("\t[FUNCTION] Chamada de função inválida! Tipos passados na chamada são:", typeParams)
            print("enquanto que os tipos definidos no método são:", list(bindable[st.PARAMS].values()), ".\n")

        # Caso seja Procedure
        elif (bindable != None and bindable[st.BINDABLE] == st.PROCEDURE):
            typeParams = pProcedureFFunctionCallStatement.exprList.accept(self)

            if (list(bindable[st.PARAMS].values()) == typeParams):
                return None

            pProcedureFFunctionCallStatement.accept(self.printer)
            print("\t[PROCEDURE] Chamada de procedimento inválida! Tipos passados na chamada são:", typeParams)
            print("enquanto que os tipos definidos no método são:", list(bindable[st.PARAMS].values()), ".\n")

#---------------------------------------------------------------------------------------

    def visitWWhileStatement(self, wWhileStatement):
        type = wWhileStatement.expr.accept(self)

        if (type != st.BOOL):
            wWhileStatement.expr.accept(self.printer)
            print("\n\t[WHILE] A expressão ", end='')
            wWhileStatement.expr.accept(self.printer)
            print(" é do tipo", type, end='')
            print(", mas deveria ser do tipo boolean.", end='\n\n')
        wWhileStatement.statement.accept(self)

#---------------------------------------------------------------------------------------

    def visitRRepeatStatement(self, rRepeatStatement):
        type = rRepeatStatement.expr.accept(self)

        if (type != st.BOOL):
            rRepeatStatement.expr.accept(self.printer)
            print("\n\t[REPEAT] A expressão ", end='')
            rRepeatStatement.expr.accept(self.printer)
            print(" é do tipo", type, end='')
            print(", mas deveria ser do tipo boolean.", end='\n\n')
        rRepeatStatement.statement.accept(self)

#---------------------------------------------------------------------------------------

    def visitFForStatement(self, fForStatement):

        # Captura ID
        bindable = st.getBindable(fForStatement.id)


        if (bindable != None and bindable[st.BINDABLE] == st.VARIABLE):
            typeExpr1 = fForStatement.expr1.accept(self)

            if bindable[st.TYPE] == st.INTEGER or bindable[st.TYPE] == st.CHAR:
                if typeExpr1 == bindable[st.TYPE]:
                    typeExpr2 = fForStatement.expr2.accept(self)

                    if typeExpr2 != bindable[st.TYPE]:
                        print("for ", fForStatement.id, ":= ", end='')
                        fForStatement.expr1.accept(self.printer)
                        print(" to ", end='')
                        fForStatement.expr2.accept(self.printer)
                        print(" do")
                        print("\t[FOR] A expressão ", end='')
                        fForStatement.expr2.accept(self.printer)
                        print(' é do tipo', typeExpr2, ", mas deveria ser do tipo", bindable[st.TYPE], end='.\n\n')
                else:
                    print("for ", fForStatement.id, ":= ", end='')
                    fForStatement.expr1.accept(self.printer)
                    print(" to ", end='')
                    fForStatement.expr2.accept(self.printer)
                    print(" do")
                    print("\n\t[FOR] A expressão ", end='')
                    fForStatement.expr1.accept(self.printer)
                    print(' é do tipo', typeExpr1, ", mas deveria ser do tipo", bindable[st.TYPE], end='.\n\n')

            else:
                print("for ", fForStatement.id, ":= ", end='')
                fForStatement.expr1.accept(self.printer)
                print(" to ", end='')
                fForStatement.expr2.accept(self.printer)
                print(" do")
                print("\n\t[FOR] A variável", fForStatement.id, "é do tipo", bindable[st.TYPE], ", mas deveria ser do tipo integer ou char.", end='\n\n')
        else:
            print("for ", fForStatement.id, ":= ", end='')
            fForStatement.expr1.accept(self.printer)
            print(" to ", end='')
            fForStatement.expr2.accept(self.printer)
            print(" do")
            print("\t[FOR] A variável", fForStatement.id, "não foi definida.")
#---------------------------------------------------------------------------------------

    def visitSSingleCase(self, sSingleCase):
        return sSingleCase.case.accept(self)


    def visitCCompoundCase(self, cCompoundCase):
        temp = cCompoundCase.case.accept(self)
        temp.update(cCompoundCase.cases.accept(self))
        return temp

    def visitCCaseStatement(self, cCaseStatement):
        type = cCaseStatement.expr.accept(self)

        if (type != st.CHAR and type != st.INTEGER):
            print("\n\t[CASE] A expressão ", end='')
            cCaseStatement.expr.accept(self.printer)
            print(" é do tipo", type, ", mas deveria ser integer ou char.")
        else:
            dict = cCaseStatement.cases.accept(self)
            for key in dict.keys():
                if dict[key] != type:

                    print("\t[CASE] O tipo da guarda", key, "é", dict[key], ", mas deveria ser do tipo", type, ".\n")


        cCaseStatement.cases.accept(self)


    def visitIIntegerCase(self, iIntegerCase):
        return {iIntegerCase.token:st.INTEGER}

    def visitCCharCase(self, cCharCase):
        return {cCharCase.token:st.CHAR}

    def visitIIdCase(self, iIDCase):
        return {iIDCase.token:st.getBindable(iIDCase.token)[st.TYPE]}


#---------------------------------------------------------------------------------------

    def visitIIfStatement(self, iIfStatement):
        type = iIfStatement.expr.accept(self)

        if (type != st.BOOL):
            iIfStatement.expr.accept(self.printer)
            print("\n\t[IF] A expressão ", end='')
            iIfStatement.expr.accept(self.printer)
            print(" é do tipo", type, end='')
            print(", mas deveria ser do tipo boolean.", end='\n\n')


        if iIfStatement.nstatement1 != None:
            iIfStatement.nstatement1.accept(self)

        if iIfStatement.nstatement2 != None:
            iIfStatement.nstatement2.accept(self)


#---------------------------------------------------------------------------------------


    def visitPPlusExp(self, pPlusExp):
        tipoExp1 = pPlusExp.exp1.accept(self)
        tipoExp2 = pPlusExp.exp2.accept(self)

        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            pPlusExp.accept(self.printer)
            print('\n\t[ERRO] Soma inválida! A expressão ', end='')
            pPlusExp.exp1.accept(self.printer)
            print(' é do tipo', tipoExp1, end=',')
            print(' enquanto a expressão ', end='')
            pPlusExp.exp2.accept(self.printer)
            print(' é do tipo', tipoExp2, end='.\n\n')
        return c


    def visitMMinusExp(self, mMinusExp):
        tipoExp1 = mMinusExp.exp1.accept(self)
        tipoExp2 = mMinusExp.exp2.accept(self)

        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            mMinusExp.accept(self.printer)
            print('\n\t[ERRO] Subtracao invalida! A expressão ', end='')
            mMinusExp.exp1.accept(self.printer)
            print(' é do tipo', tipoExp1, end=',')
            print(' enquanto a expressão ', end='')
            mMinusExp.exp2.accept(self.printer)
            print(' é do tipo', tipoExp2, end='.\n\n')
        return c


    def visitTTimesExp(self, tTimesExp):
        tipoExp1 = tTimesExp.exp1.accept(self)
        tipoExp2 = tTimesExp.exp2.accept(self)

        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            tTimesExp.accept(self.printer)
            print('\n\t[ERRO] Multiplicação invalida! A expressão ', end='')
            tTimesExp.exp1.accept(self.printer)
            print(' é do tipo', tipoExp1, end=',')
            print(' enquanto a expressão ', end='')
            tTimesExp.exp2.accept(self.printer)
            print(' é do tipo', tipoExp2, '.\n')
        return c


    def visitDDivideExp(self, dDivideExp):
        tipoExp1 = dDivideExp.exp1.accept(self)
        tipoExp2 = dDivideExp.exp2.accept(self)

        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            dDivideExp.accept(self.printer)
            print('\n\t[ERRO] Divisão invalida. A expressão ', end='')
            dDivideExp.exp1.accept(self.printer)
            print(' é do tipo', tipoExp1, end=',')
            print(' enquanto a expressão ', end='')
            dDivideExp.exp2.accept(self.printer)
            print(' é do tipo', tipoExp2, end='.\n\n')
        return c


    def visitDDivExp(self, dDivExp):
        tipoExp1 = dDivExp.exp1.accept(self)
        tipoExp2 = dDivExp.exp2.accept(self)

        c = coercionDDivExp(tipoExp1, tipoExp2)
        if (c == None):
            dDivExp.accept(self.printer)
            print('\n\t[ERRO] Divisão invalida! A expressão ', end='')
            dDivExp.exp1.accept(self.printer)
            print(' é do tipo', tipoExp1, end=',')
            print(' enquanto a expressão ', end='')
            dDivExp.exp2.accept(self.printer)
            print(' é do tipo', tipoExp2, end='.\n\n')
        return c


    def visitMModExp(self, mModExp):
        tipoExp1 = mModExp.exp1.accept(self)
        tipoExp2 = mModExp.exp2.accept(self)

        c = coercion(tipoExp1, tipoExp2)
        if (c == None):
            mModExp.accept(self.printer)
            print('\n\t[ERRO] Divisão invalida! A expressão ', end='')
            mModExp.exp1.accept(self.printer)
            print(' é do tipo', tipoExp1, end=',')
            print(' enquanto a expressão ', end='')
            mModExp.exp2.accept(self.printer)
            print(' é do tipo', tipoExp2, end='.\n\n')
        return c


    def visitEEqualsExp(self, eEqualsExp):
        tipoExp1 = eEqualsExp.exp1.accept(self)
        tipoExp2 = eEqualsExp.exp2.accept(self)

        c = validaTipo(tipoExp1, tipoExp2)
        if (c == None):
            eEqualsExp.accept(self.printer)
            print('\n\t[ERRO: =] Comparação inválida! A expressão ', end='')
            eEqualsExp.exp1.accept(self.printer)
            print(' é do tipo', tipoExp1, end=',')
            print(' enquanto a expressão ', end='')
            eEqualsExp.exp2.accept(self.printer)
            print(' é do tipo', tipoExp2, end='.\n\n')
        return c


    def visitDDifferentExp(self, dDifferentExp):
        tipoExp1 = dDifferentExp.exp1.accept(self)
        tipoExp2 = dDifferentExp.exp2.accept(self)

        c = validaTipo(tipoExp1, tipoExp2)
        if (c == None):
            dDifferentExp.accept(self.printer)
            print('\n\t[ERRO: <>] Comparação inválida! A expressão ', end='')
            dDifferentExp.exp1.accept(self.printer)
            print(' é do tipo', tipoExp1, end=',')
            print(' enquanto a expressão ', end='')
            dDifferentExp.exp2.accept(self.printer)
            print(' é do tipo', tipoExp2, end='.\n\n')
        return c


    def visitLLthanExp(self, lLthanExp):
        tipoExp1 = lLthanExp.exp1.accept(self)
        tipoExp2 = lLthanExp.exp2.accept(self)

        c = validaExpressaoNumerica(tipoExp1, tipoExp2)
        if (c == None):
            lLthanExp.accept(self.printer)
            print('\n\t[ERRO: <] Comparacão inválida! A expressão ', end='')
            lLthanExp.exp1.accept(self.printer)
            print(' é do tipo', tipoExp1, end=',')
            print(' enquanto a expressao ', end='')
            lLthanExp.exp2.accept(self.printer)
            print(' é do tipo', tipoExp2, end='.\n\n')
        return c


    def visitGGthanExp(self, gGthanExp):
        tipoExp1 = gGthanExp.exp1.accept(self)
        tipoExp2 = gGthanExp.exp2.accept(self)

        c = validaExpressaoNumerica(tipoExp1, tipoExp2)
        if (c == None):
            gGthanExp.accept(self.printer)
            print('\n\t[ERRO: >] Comparação inválida! A expressão ', end='')
            gGthanExp.exp1.accept(self.printer)
            print(' é do tipo', tipoExp1, end=',')
            print(' enquanto a expressão ', end='')
            gGthanExp.exp2.accept(self.printer)
            print(' é do tipo', tipoExp2, end='.\n\n')
        return c


    def visitGGequals(self, gGequals):
        tipoExp1 = gGequals.exp1.accept(self)
        tipoExp2 = gGequals.exp2.accept(self)

        c = validaExpressaoNumerica(tipoExp1, tipoExp2)
        if (c == None):
            gGequals.accept(self.printer)
            print('\n\t[ERRO: >=] Comparacão inválida. A expressão ', end='')
            gGequals.exp1.accept(self.printer)
            print(' é do tipo', tipoExp1, end=',')
            print(' enquanto a expressão ', end='')
            gGequals.exp2.accept(self.printer)
            print(' é do tipo', tipoExp2, end='.\n\n')
        return c


    def visitLLequalsExp(self, lLequalsExp):
        tipoExp1 = lLequalsExp.exp1.accept(self)
        tipoExp2 = lLequalsExp.exp2.accept(self)

        c = validaExpressaoNumerica(tipoExp1, tipoExp2)
        if (c == None):
            lLequalsExp.accept(self.printer)
            print('\n\t[ERRO: <=] Comparacão inválida! A expressão ', end='')
            lLequalsExp.exp1.accept(self.printer)
            print(' é do tipo', tipoExp1, end=',')
            print(' enquanto a expressão ', end='')
            lLequalsExp.exp2.accept(self.printer)
            print(' é do tipo', tipoExp2, end='.\n\n')
        return c


    def visitAAndExp(self, aAndExp):
        tipoExp1 = aAndExp.exp1.accept(self)
        tipoExp2 = aAndExp.exp2.accept(self)

        c = validaExpressaoBooleana(tipoExp1, tipoExp2)
        if (c == None):
            aAndExp.accept(self.printer)
            print('\n\t[ERRO: AND] Comparacão inválida! A expressão ', end='')
            aAndExp.exp1.accept(self.printer)
            print(' é do tipo', tipoExp1, end=',')
            print(' enquanto a expressão ', end='')
            aAndExp.exp2.accept(self.printer)
            print(' é do tipo', tipoExp2, end='.\n\n')
        return c

    def visitOOrExp(self, oOrExp):
        tipoExp1 = oOrExp.exp1.accept(self)
        tipoExp2 = oOrExp.exp2.accept(self)

        c = validaExpressaoBooleana(tipoExp1, tipoExp2)
        if (c == None):
            oOrExp.accept(self.printer)
            print('\n\t[ERRO: OR] Comparacão inválida! A expressão ', end='')
            oOrExp.exp1.accept(self.printer)
            print(' é do tipo', tipoExp1, end=',')
            print(' enquanto a expressão ', end='')
            oOrExp.exp2.accept(self.printer)
            print(' é do tipo', tipoExp2, end='.\n\n')
        return c


    def visitUPPlusExp(self, uPPlusExp):
        tipoExp1 = uPPlusExp.exp.accept(self)

        c = validaUnaria(tipoExp1)
        if (c == None):
            uPPlusExp.accept(self.printer)
            print('\n\t[ERRO: UPLUS] Expressão unária inválida: ', end='')
            uPPlusExp.accept(self.printer)
            print("! Operador unário só pode ser utilizado com números.", end="\n\n")
        return c


    def visitUMMinusExp(self, uMMinusExp):
        tipoExp1 = uMMinusExp.exp.accept(self)

        c = validaUnaria(tipoExp1)
        if (c == None):
            uMMinusExp.accept(self.printer)
            print('\n\t[ERRO: UMINUS] Expressão unária inválida: ', end='')
            uMMinusExp.accept(self.printer)
            print("! Operador unário só pode ser utilizado com números.", end='\n\n')
        return c


    def visitFFactorString(self, fFactorString):
        return st.STRING

    def visitFFactorInt(self, fFactorInt):
        return st.INTEGER

    def visitFFactorChar(self, fFactorChar):
        return st.CHAR

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
        type = fFactorNot.literal.accept(self)
        if type == st.BOOL:
            return type
        else:
            print("Não é possível aplicar o operador not em uma expressão não booleana.")
            return None

