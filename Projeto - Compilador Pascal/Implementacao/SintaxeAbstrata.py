from abc import abstractmethod
from abc import ABCMeta
from Visitor import Visitor



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
        visitor.visitPProgram(self)



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
        visitor.visitBBlock(self)



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
        visitor.visitCConstDefinition(self)




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
        visitor.visitVVarDeclaration(self)



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
        visitor.visitPProcedureDeclaration(self)



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
        visitor.visitFFunctionDeclaration(self)




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
        visitor.visitCCompoundStatementScore(self)


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
        visitor.visitCCompoundStatementSemicolon(self)


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
        visitor.visitSSingleStatement(self)

class CCompoundStatement(Statements):
    def __init__(self, statementt, statementss):
        self.statementt = statementt
        self.statementss = statementss

    def accept(self, visitor):
        visitor.visitCCompoundStatement(self)




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
        visitor.visitAAssignStatement(self)


class PProcedureCallStatement(Statement):
    def __init__(self, id, exprList):
        self.id = id
        self.exprList = exprList

    def accept(self, visitor):
        visitor.visitPProcedureCallStatement(self)


class IIfStatement(Statement):
    def __init__(self, expr_list, nstatement1, nstatement2):
        self.expr_list = expr_list
        self.nstatement1 = nstatement1
        self.nstatement2 = nstatement2

    def accept(self, visitor):
        visitor.visitIIfStatement(self)


class WWhileStatement(Statement):
    def __init__(self, expr, statement):
        self.expr = expr
        self.statement = statement

    def accept(self, visitor):
        visitor.visitWWhileStatement(self)


class RRepeatStatement(Statement):
    def __init__(self, statement, expr):
        self.statement = statement
        self.expr = expr

    def accept(self, visitor):
        visitor.visitRRepeatStatement(self)


class FForStatement(Statement):
    def __init__(self, id, expr1, expr2, statement):
        self.id = id
        self.expr1 = expr1
        self.expr2 = expr2
        self.statement = statement

    def accept(self, visitor):
        visitor.visitFForStatement(self)


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
        visitor.visitSingleCase(self)


class CCompoundCase(Cases):
    def __init__(self, case, cases):
        self.case = case
        self.cases = cases

    def accept(self, visitor):
        visitor.visitCCompoundCase(self)


'''
Case e classes concretas
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
        visitor.visitIntegerCase(self)


class RRealCase(Case):
    def __init__(self, token, statement):
        self.token = token
        self.statement = statement

    def accept(self, visitor):
        visitor.visitRealCase(self)


class IIdCase(Case):
    def __init__(self, token, statement):
        self.token = token
        self.statement = statement

    def accept(self, visitor):
        visitor.visitIIdCase(self)


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
        visitor.visitSingleExprList(self)


class CCompoundExprList(ExprList):
    def __init__(self, expr1, expr2):
        self.expr1 = expr1
        self.expr2 = expr2

    def accept(self, visitor):
        visitor.visitCCompoundExprList(self)




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
        visitor.visitEEqualsExp(self)

class LLthanExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        visitor.visitLLthanExp(self)

class GGthanExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        visitor.visitGGthanExp(self)

class DDifferentExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        visitor.visitDDifferentExp(self)

class GGequals(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        visitor.visitGGequals(self)

class LLequalsExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        visitor.visitLLequalsExpp(self)

class PPlusExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        visitor.visitPPlusExp(self)


class MMinusExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        visitor.visitMMinusExp(self)

class OOrExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        visitor.visitOOrExp(self)


class TTimesExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        visitor.visitTTimesExp(self)


class DDivideExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        visitor.visitDDivideExp(self)


class DDivExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        visitor.visitDDivExp(self)


class MModExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        visitor.visitMModExp(self)


class AAndExp(Expressao):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2

    def accept(self, visitor):
        visitor.visitAAndExp(self)


class UPPlusExp(Expressao):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        visitor.visitUPPlusExp(self)


class UMMinusExp(Expressao):
    def __init__(self, exp):
        self.exp = exp

    def accept(self, visitor):
        visitor.visitUMMinusExp(self)




'''
Factor e classes concretas
'''
class Factor(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, Visitor):
        pass


class FFactorString(Expressao):
    def __init__(self, type):
        self.type = type

    def accept(self, visitor):
        visitor.visitFFactorString(self)


class FFactorInt(Expressao):
    def __init__(self, type):
        self.type = type

    def accept(self, visitor):
        visitor.visitFFactorInt(self)


class FFactorReal(Expressao):
    def __init__(self, type):
        self.type = type

    def accept(self, visitor):
        visitor.visitFFactorReal(self)


class FFactorId(Expressao):
    def __init__(self, type):
        self.type = type

    def accept(self, visitor):
        visitor.visitFFactorId(self)


class FFactorNot(Expressao):
    def __init__(self, type):
        self.type = type

    def accept(self, visitor):
        visitor.visitFFactorNot(self)



