from abc import abstractmethod
from abc import ABCMeta
from Visitor import Visitor

'''
Exp e classes concretas
'''
class Exp(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class SomaExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        visitor.visitSomaExp(self)


class MulExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        visitor.visitMulExp(self)


class PotExp(Exp):
    def __init__(self, exp1, exp2):
        self.exp1 = exp1
        self.exp2 = exp2
    def accept(self, visitor):
        visitor.visitPotExp(self)


class CallExp(Exp):
    def __init__(self, call):
        self.call = call

    def accept(self, visitor):
        visitor.visitCallExp(self)

class AssignExp(Exp):
    def __init__(self, assign):
        self.assign = assign
    def accept(self, visitor):
        visitor.visitAssignExp(self)


class NumExp(Exp):
    def __init__(self, num):
        self.num = num
    def accept(self, visitor):
        visitor.visitNumExp(self)


class IdExp(Exp):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        visitor.visitIdExp(self)


'''
Call e classes concretas
'''
class Call(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class ParamsCall(Call):
    def __init__ (self, id, params):
        self.id = id
        self.params = params
    def accept(self, visitor):
        visitor.visitParamsCall(self)

class SimpleCall(Call):
    def __init__(self, id):
        self.id = id
    def accept(self, visitor):
        visitor.visitSimpleCall(self)


'''
Params e classes concretas
'''
class Params(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class CompoundParams(Params):
    def __init__(self, exp, params):
        self.exp = exp
        self.params = params
    def accept(self, visitor):
        visitor.visitCompoundParams(self)

class SingleParam(Params):
    def __init__(self, exp):
        self.exp = exp
    def accept(self, visitor):
        visitor.visitSingleParam(self)


'''
Assign e classes concretas
'''
class Assign(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, visitor):
        pass

class AssignAss(Assign):
    def __init__(self, id, exp):
        self.id = id
        self.exp = exp
    def accept(self, visitor):
        visitor.visitAssignAss(self)
