from abc import abstractmethod
from abc import ABCMeta
#from Visitor import Visitor
from SemanticVisitor import SemanticVisitor


'''
Program e classes concretas
'''
class Program(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class PProgram(Program):
    def __init__(self, id, block):
        self.block = block
        self.id = id
    def accept(self, visitor):
        return visitor.visitPProgram(self)



'''
Block e classes concretas
'''

class  Block(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class BBlock(Block):
    def __init__(self, const_dec, var_dec, subroutine_dec, compoundStatement_dec):
        self.const_dec = const_dec
        self.var_dec = var_dec
        self.subroutine_dec = subroutine_dec
        self.compoundStatement_dec = compoundStatement_dec

    def accept(self, visitor):
        return visitor.visitBBlock(self)



'''
Const e classes concretas
'''

class  ConstDefinition(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class CConstDefinition(ConstDefinition):
    def __init__(self, dicDefinicoes):
        self.dicDefinicoes = dicDefinicoes
    def accept(self, visitor):
        return visitor.visitCConstDefinition(self)




'''
Var e classes concretas
'''
class VarDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass


class VVarDeclaration(VarDeclaration):
    def __init__(self, dicDefinicoes):
        self.dicDefinicoes = dicDefinicoes
    def accept(self, visitor):
        return visitor.visitVVarDeclaration(self)



'''
Procedure e classes concretas
'''
class ProcedureDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass


class PProcedureDeclaration(ProcedureDeclaration):
    def __init__(self, dicDefinicoes):
        self.dicDefinicoes = dicDefinicoes
    def accept(self, visitor):
        return visitor.visitPProcedureDeclaration(self)



'''
Function e classes concretas
'''
class FunctionDeclaration(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass


class FFunctionDeclaration(FunctionDeclaration):
    def __init__(self, dicDefinicoes, id):
        self.dicDefinicoes = dicDefinicoes
        self.id = id
    def accept(self, visitor):
        return visitor.visitFFunctionDeclaration(self)




'''
CompoundStatementScore e classes concretas
'''
class CompoundStatementScore(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class CCompoundStatementScore(CompoundStatementScore):
    def __init__(self, statements):
        self.statements = statements

    def accept(self, visitor):
        return visitor.visitCCompoundStatementScore(self)


'''
CompoundStatementSemicolon e classes concretas
'''
class CompoundStatementSemicolon(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class CCompoundStatementSemicolon(CompoundStatementSemicolon):
    def __init__(self, statements):
        self.statements = statements

    def accept(self, visitor):
        return visitor.visitCCompoundStatementSemicolon(self)


'''
Statements e classes concretas
'''
class Statements(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class SSingleStatement(Statements):
    def __init__(self, statementt):
        self.statementt = statementt

    def accept(self, visitor):
        return visitor.visitSSingleStatement(self)

class CCompoundStatement(Statements):
    def __init__(self, statementt, statementss):
        self.statementt = statementt
        self.statementss = statementss

    def accept(self, visitor):
        return visitor.visitCCompoundStatement(self)




'''
Statement e classes concretas
'''
class Statement(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class AAssignStatement(Statement):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitAAssignStatement(self)


class PProcedureFFunctionCallStatement(Statement):
    def __init__(self, id, exprList):
        self.id = id
        self.exprList = exprList

    def accept(self, visitor):
        return visitor.visitPProcedureFFunctionCallStatement(self)


class WWhileStatement(Statement):
    def __init__(self, expr, statement):
        self.expr = expr
        self.statement = statement

    def accept(self, visitor):
        return visitor.visitWWhileStatement(self)


class RRepeatStatement(Statement):
    def __init__(self, statement, expr):
        self.statement = statement
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitRRepeatStatement(self)


class FForStatement(Statement):
    def __init__(self, id, expr1, expr2, statement):
        self.id = id
        self.expr1 = expr1
        self.expr2 = expr2
        self.statement = statement

    def accept(self, visitor):
        return visitor.visitFForStatement(self)


class CCaseStatement(Statement):
    def __init__(self, expr, cases):
        self.expr = expr
        self.cases = cases

    def accept(self, visitor):
        return visitor.visitCCaseStatement(self)


class IIfStatement(Statement):
    def __init__(self, expr, nstatement1, nstatement2):
        self.expr = expr
        self.nstatement1 = nstatement1
        self.nstatement2 = nstatement2

    def accept(self, visitor):
        return visitor.visitIIfStatement(self)


'''
Cases e classes concretas
'''
class Cases(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass


class SSingleCase(Cases):
    def __init__(self, case):
        self.case = case

    def accept(self, visitor):
        return visitor.visitSSingleCase(self)


class CCompoundCase(Cases):
    def __init__(self, case, cases):
        self.case = case
        self.cases = cases

    def accept(self, visitor):
        return visitor.visitCCompoundCase(self)


'''
Tipos de Case e classes concretas
'''
class Case(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass


class IIntegerCase(Case):
    def __init__(self, token, statement):
        self.token = token
        self.statement = statement

    def accept(self, visitor):
        return visitor.visitIIntegerCase(self)


class RRealCase(Case):
    def __init__(self, token, statement):
        self.token = token
        self.statement = statement

    def accept(self, visitor):
        return visitor.visitRRealCase(self)


class IIdCase(Case):
    def __init__(self, token, statement):
        self.token = token
        self.statement = statement

    def accept(self, visitor):
        return visitor.visitIIdCase(self)


'''
ExprList e classes concretas
'''
class ExprList(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass

class SSingleExprList(ExprList):
    def __init__(self, expr):
        self.expr = expr

    def accept(self, visitor):
        return visitor.visitSSingleExprList(self)


class CCompoundExprList(ExprList):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def accept(self, visitor):
        return visitor.visitCCompoundExprList(self)




'''
Expressão e classes concretas
'''
class Expressao(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass


class EEqualsExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        return visitor.visitEEqualsExp(self)

class LLthanExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitLLthanExp(self)

class GGthanExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitGGthanExp(self)

class DDifferentExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitDDifferentExp(self)

class GGequals(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitGGequals(self)

class LLequalsExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitLLequalsExp(self)

class PPlusExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitPPlusExp(self)


class MMinusExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitMMinusExp(self)

class OOrExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitOOrExp(self)


class TTimesExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitTTimesExp(self)


class DDivideExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitDDivideExp(self)


class DDivExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitDDivExp(self)


class MModExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitMModExp(self)


class AAndExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        return visitor.visitAAndExp(self)


class UPPlusExp(Expressao):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitUPPlusExp(self)


class UMMinusExp(Expressao):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        return visitor.visitUMMinusExp(self)



class FFactorString(Expressao):
    def __init__(self, literal):
        self.literal = literal

    def accept(self, visitor):
        return visitor.visitFFactorString(self)

class FFactorChar(Expressao):
    def __init__(self, literal):
        self.literal = literal

    def accept(self, visitor):
        return visitor.visitFFactorChar(self)


class FFactorInt(Expressao):
    def __init__(self, literal):
        self.literal = literal

    def accept(self, visitor):
        return visitor.visitFFactorInt(self)


class FFactorReal(Expressao):
    def __init__(self, literal):
        self.literal = literal

    def accept(self, visitor):
        return visitor.visitFFactorReal(self)


class FFactorId(Expressao):
    def __init__(self, literal):
        self.literal = literal

    def accept(self, visitor):
        return visitor.visitFFactorId(self)


class FFactorBoolean(Expressao):
    def __init__(self, literal):
        self.literal = literal

    def accept(self, visitor):
        return visitor.visitFFactorBoolean(self)


class FFactorNot(Expressao):
    def __init__(self, literal):
        self.literal = literal

    def accept(self, visitor):
        return visitor.visitFFactorNot(self)



