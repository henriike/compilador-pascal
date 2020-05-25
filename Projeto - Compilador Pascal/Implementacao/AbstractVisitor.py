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
    def visitPPlusExp(self, pPlusExp):
        pass

