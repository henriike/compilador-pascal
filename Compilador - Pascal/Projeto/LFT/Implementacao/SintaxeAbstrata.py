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