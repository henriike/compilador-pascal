from AbstractVisitor import AbstractVisitor
import SymbolTable as st
from Visitor import Visitor
from SymbolTable import *

import SintaxeAbstrata as sa

def coercion(type1, type2):
    if (type1 in st.Number and type2 in st.Number):
        if (type1 == st.FLOAT or type2 == st.FLOAT):
            return st.FLOAT
        else:
            return st.INT
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
                addConst(i, cConstDefinition.dicDefinicoes[i])



    def visitVVarDeclaration(self, vVarDeclaration):
        if vVarDeclaration != None:
            for i in vVarDeclaration.dicDefinicoes.keys():
                addVar(i, vVarDeclaration.dicDefinicoes[i])



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



    def visitFFunctionDeclaration(self, fFunctionDeclaration):
        if fFunctionDeclaration != None:
            for key, v in fFunctionDeclaration.dicDefinicoes.items():
                dic = translateToDicParams(key)
                addFunction(fFunctionDeclaration.id, dic, v)



    def visitPProcedureDeclaration(self, pProcedureDeclaration):
        if pProcedureDeclaration != None:
            for key, v in pProcedureDeclaration.dicDefinicoes.items():
                dic = translateToDicParams(key)
                addProcedure(pProcedureDeclaration.dicDefinicoes.keys()[0], dic)