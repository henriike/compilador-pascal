class Visitor:
    def visitSomaExp(self, somaExp):
        # print("visitSomaExp")
        somaExp.exp1.accept(self)
        print(' + ', end='')
        somaExp.exp2.accept(self)

    def visitMulExp(self, mulExp):
        # print("visitMulExp")
        mulExp.exp1.accept(self)
        print(' * ', end='')
        mulExp.exp2.accept(self)

    def visitPotExp(self, potExp):
        # print("visitPotExp")
        potExp.exp1.accept(self)
        print(' ^ ', end='')
        potExp.exp2.accept(self)

    def visitAssignExp(self, assignExp):
        # print("visitAssignExp")
        assignExp.assign.accept(self)

    def visitIdExp(self, idExp):
        # print("visitIdExp")
        print(idExp.id, end='')

    def visitNumExp(self, numExp):
        # print("visitNumExp")
        print(numExp.num, end='')

    def visitCallExp(self, callExp):
        # print("visitCallExp")
        callExp.call.accept(self)

    def visitSimpleCall(self, simpleCall):
        # print("visitSimpleCall")
        print(simpleCall.id, '()', end='')

    def visitParamsCall(self, paramsCall):
        # print("visitParamsCall")
        print(paramsCall.id, '(', end='')
        paramsCall.params.accept(self)
        print(')', end='')

    def visitAssignAss(self, assignAss):
        # print("visitAssignAss")
        print(assignAss.id, ' = ', end='')
        assignAss.exp.accept(self)
        print('')

    def visitSingleParam(self, singleParam):
        # print("visitSingleParam")
        singleParam.exp.accept(self)

    def visitCompoundParams(self, compoundParams):
        # print("visitCompoundParams")
        compoundParams.exp.accept(self)
        print(', ', end='')
        compoundParams.params.accept(self)
