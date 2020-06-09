from abc import abstractmethod
from abc import ABCMeta

class AbstractVisitor(metaclass=ABCMeta):

    @abstractmethod
    def visitPProgram(self, pProgram):
        pass

    @abstractmethod
    def visitBBlock(self, bBlock):
        pass

    @abstractmethod
    def visitCConstDefinition(self, cConstDefiniton):
        pass

    @abstractmethod
    def visitVVarDeclaration(self, vVarDeclaration):
        pass

    @abstractmethod
    def visitPProcedureDeclaration(self, pProcedureDeclaration):
        pass

    @abstractmethod
    def visitFFunctionDeclaration(self, fFunctionDeclaration):
        pass

    @abstractmethod
    def visitCCompoundStatementScore(self, cCompoundStatementScore):
        pass

    @abstractmethod
    def visitCCompoundStatementSemicolon(self, cCompoundStatementSemicolon):
        pass

    @abstractmethod
    def visitSSingleStatement(self, sSingleStatement):
        pass

    @abstractmethod
    def visitCCompoundStatement(self, cCompoundStatement):
        pass

    @abstractmethod
    def visitSSingleExprList(self, sSingleExprList):
        pass

    @abstractmethod
    def visitCCompoundExprList(self, cCompoundExprList):
        pass

    @abstractmethod
    def visitAAssignStatement(self, aAssignStatement):
        pass

    @abstractmethod
    def visitPProcedureFFunctionCallStatement(self, pProcedureFFunctionCallStatement):
        pass

    @abstractmethod
    def visitWWhileStatement(self, wWhileStatement):
        pass

    @abstractmethod
    def visitRRepeatStatement(self, rRepeatStatement):
        pass

    @abstractmethod
    def visitFForStatement(self, fForStatement):
        pass

    @abstractmethod
    def visitSSingleCase(self, sSingleCase):
        pass

    @abstractmethod
    def visitCCompoundCase(self, cCompoundCase):
        pass

    @abstractmethod
    def visitCCaseStatement(self, cCaseStatement):
        pass

    @abstractmethod
    def visitIIntegerCase(self, iIntegerCase):
        pass

    @abstractmethod
    def visitRRealCase(self, rRealCase):
        pass

    @abstractmethod
    def visitIIdCase(self, iIdCase):
        pass

    @abstractmethod
    def visitIIfStatement(self, iIfStatement):
        pass

    @abstractmethod
    def visitPPlusExp(self, pPlusExp):
        pass

    @abstractmethod
    def visitMMinusExp(self, mMinusExp):
        pass

    @abstractmethod
    def visitTTimesExp(self, tTimesExp):
        pass

    @abstractmethod
    def visitDDivideExp(self, dDivideExp):
        pass

    @abstractmethod
    def visitDDivExp(self, dDivExp):
        pass

    @abstractmethod
    def visitMModExp(self, mModExp):
        pass

    @abstractmethod
    def visitEEqualsExp(self, eEqualsExp):
        pass

    @abstractmethod
    def visitDDifferentExp(self, dDifferentExp):
        pass

    @abstractmethod
    def visitLLthanExp(self, lLthanExp):
        pass

    @abstractmethod
    def visitGGthanExp(self, gGthanExp):
        pass

    @abstractmethod
    def visitGGequals(self, gGequals):
        pass

    @abstractmethod
    def visitLLequalsExp(self, lLequalsExp):
        pass

    @abstractmethod
    def visitAAndExp(self, aAndExp):
        pass

    @abstractmethod
    def visitOOrExp(self, oOrExp):
        pass

    @abstractmethod
    def visitUPPlusExp(self, uPPlusExp):
        pass

    @abstractmethod
    def visitUMMinusExp(self, uMMinusExp):
        pass

    @abstractmethod
    def visitFFactorString(self, fFactorString):
        pass

    @abstractmethod
    def visitFFactorInt(self, fFactorInt):
        pass

    @abstractmethod
    def visitFFactorReal(self, fFactorReal):
        pass

    @abstractmethod
    def visitFFactorId(self, fFactorId):
        pass

    @abstractmethod
    def visitFFactorBoolean(self, fFactorBoolean):
        pass

    @abstractmethod
    def visitFFactorNot(self, fFactorNot):
        pass
