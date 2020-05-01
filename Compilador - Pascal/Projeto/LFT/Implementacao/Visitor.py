class Visitor:

    def visitPProgram(self, pProgram):
        if (pProgram.block != None):
            print('program', pProgram.id, ';')
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
            print('const')
            indices = list(cConstDefinition.dicDefinicoes.keys())
            indices = reversed(indices)
            for key in indices:
                print(key,' = ', cConstDefinition.dicDefinicoes[key], ';')


    def visitVVarDeclaration(self, vVarDeclaration):
        if vVarDeclaration != None:
            print('var')
            indices = list(vVarDeclaration.dicDefinicoes.keys())
            indices = reversed(indices)
            for key in indices:
                print(key,' : ', vVarDeclaration.dicDefinicoes[key], ';')


    def visitPProcedureDeclaration(self, pProcedureDeclaration):
        if pProcedureDeclaration != None:
            indices = list(pProcedureDeclaration.dicDefinicoes.keys())
            indices = reversed(indices)
            for key in indices:
                print('procedure', key, ' ( ', pProcedureDeclaration.dicDefinicoes[key], ' ) ;')


    def visitFFunctionDeclaration(self, fFunctionDeclaration):
        if fFunctionDeclaration != None:
            for key, v in fFunctionDeclaration.dicDefinicoes.items():
                print('function', fFunctionDeclaration.id, ' ( ', key, ' ) : ', v, ' ; ')




    # Visitor do Compound

    #def visitCCompoundStatementScore():





    # Visitor do ExprList

    def visitSSingleExprList(self, sSingleExprList):
        print(sSingleExprList.expr, end='')

    def visitCCompoundExprList(self, CCompoundExprList):
        CCompoundExprList.expr1(self)
        print(' , ', end='')
        CCompoundExprList.expr2(self)



    # Visitor das Expressões

    def visitEEqualsExp(self, eEqualsExp):
        eEqualsExp.exp1(self)
        print(' + ', end='')
        eEqualsExp.exp2(self)

    def visitLLthanExp(self, lLthanExp):
        lLthanExp.exp1(self)
        print(' < ', end='')
        lLthanExp.exp2(self)

    def visitGGthanExp(self, gGthanExp):
        gGthanExp.exp1(self)
        print(' > ', end='')
        gGthanExp.exp2(self)

    def visitDDifferentExp(self, dDifferentExp):
        dDifferentExp.exp1(self)
        print(' <> ', end='')
        dDifferentExp.exp2(self)

    def visitGGequals(self, gGequals):
        gGequals.exp1(self)
        print(' >= ', end='')
        gGequals.exp2(self)

    def visitLLequalsExp(self, lLequalsExp):
        lLequalsExp.exp1(self)
        print(' <= ', end='')
        lLequalsExp.exp2(self)

    def visitPPlusExp(self, pPlusExp):
        pPlusExp.exp1(self)
        print(' + ', end='')
        pPlusExp.exp2(self)

    def visitMMinusExp(self, mMinusExp):
        mMinusExp.exp1(self)
        print(' - ', end='')
        mMinusExp.exp2(self)

    def visitOOrExp(self, oOrExp):
        oOrExp.exp1(self)
        print(' or ', end='')
        oOrExp.exp2(self)

    def visitTTimesExp(self, tTimesExp):
        tTimesExp.exp1(self)
        print(' * ', end='')
        tTimesExp.exp2(self)

    def visitDDivideExp(self, dDivideExp):
        dDivideExp.exp1(self)
        print(' / ', end='')
        dDivideExp.exp2(self)

    def visitDDivExp(self, dDivExp):
        dDivExp.exp1(self)
        print(' div ', end='')
        dDivExp.exp2(self)

    def vistiMModExp(self, mModExp):
        mModExp.exp1(self)
        print(' mod ', end='')
        mModExp.exp2(self)

    def visitAAndExp(self, aAndExp):
        aAndExp.exp1(self)
        print(' and ', end='')
        aAndExp.exp2(self)

    def visitUPPlusExp(self, uPPlusExp):
        print('+', end='')
        uPPlusExp.exp(self)

    def visitUMMinusExp(self, uMMinusExp):
        print('-', end='')
        uMMinusExp.exp(self)


    # Visitor do Factor

    def visitFFactorString(self, fFactorString):
        print(fFactorString.type, end='')

    def visitFFactorInt(self, fFactorInt):
        print(fFactorInt.type, end='')

    def visitFFactorReal(self, fFactorReal):
        print(fFactorReal.type, end='')

    def visitFFactorId(self, fFactorId):
        print(fFactorId.type, end='')

    def visitFFactorNot(self, fFactorNot):
        print(' not ', fFactorNot.type, end='')



    #--------------------------------------------------------------------------------------------


    def visitAAssignStatement(self, aAssignStatement):
        if aAssignStatement != None:
            aAssignStatement.id.accept(self)
            print(':=')
            aAssignStatement.exp.accept(self)
            print(';')


    def visitPProcedureCall(self, pProcedureCall):
        if pProcedureCall != None:
            pProcedureCall.id.accept(self)
            print('(', pProcedureCall.exprList, ');')


    def visitWWhileStatement(self, wWhileStatement):
        print('while', wWhileStatement.exp, 'do')
        wWhileStatement.statement.accept(self)


    # p[0] = dict({p[1]: p[3]}.items() + p[0].items())
    # Gera um novo dicionário, inserindo os dados corretamente (organizado)