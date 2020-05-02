class Visitor:

    # Visitor do Program

    def visitPProgram(self, pProgram):
        if (pProgram.block != None):
            print('program', pProgram.id, ';')
            pProgram.block.accept(self)


    # Visitor do Block

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


    # Visitor do Const

    def visitCConstDefinition(self, cConstDefinition):
        if cConstDefinition != None:
            print('const')
            indices = list(cConstDefinition.dicDefinicoes.keys())
            indices = reversed(indices)
            for key in indices:
                print(key,' = ', cConstDefinition.dicDefinicoes[key], ';')


    # Visitor do Var

    def visitVVarDeclaration(self, vVarDeclaration):
        if vVarDeclaration != None:
            print('var')
            indices = list(vVarDeclaration.dicDefinicoes.keys())
            indices = reversed(indices)
            for key in indices:
                print(key,' : ', vVarDeclaration.dicDefinicoes[key], ';')


    # Visitor do Procedure

    def visitPProcedureDeclaration(self, pProcedureDeclaration):
        if pProcedureDeclaration != None:
            indices = list(pProcedureDeclaration.dicDefinicoes.keys())
            indices = reversed(indices)
            for key in indices:
                print('procedure', key, ' ( ', pProcedureDeclaration.dicDefinicoes[key], ' ) ;')


    # Visitor do Function

    def visitFFunctionDeclaration(self, fFunctionDeclaration):
        if fFunctionDeclaration != None:
            for key, v in fFunctionDeclaration.dicDefinicoes.items():
                print('function', fFunctionDeclaration.id, ' ( ', key, ' ) : ', v, ' ; ')



    # Visitor do CompoundStatementScore

    def visitCCompoundStatementScore(self, cCompoundStatementScore):
        if cCompoundStatementScore != None:
            print('begin', end='')
            cCompoundStatementScore.statements(self)
            print('end.', end='')



    # Visitor do CompoundStatementSemicolon

    def visitCCompoundStatementSemicolon(self, cCompoundStatementSemicolon):
        if cCompoundStatementSemicolon != None:
            print('begin', end='')
            cCompoundStatementSemicolon.statements(self)
            print('end;', end='')



    # Visitor do Statements

    def visitSSingleStatement(self, sSingleStatement):
        if sSingleStatement != None:
            sSingleStatement.statementt(self)

    def visitCCompoundStatement(self, cCompoundStatement):
        if cCompoundStatement != None:
            cCompoundStatement.statementt(self)
            print(' ', end='')
            cCompoundStatement.statementss(self)



    # Visitor do Statement

    def visitAAssignStatement(self, aAssignStatement):
        if aAssignStatement != None:
            aAssignStatement.id(self)
            print(' := ', end='')
            aAssignStatement.exp(self)
            print(';', end='')


    def visitPProcedureCallStatement(self, pProcedureCallStatement):
        if pProcedureCallStatement != None:
            pProcedureCallStatement.id(self)
            print('( ', end='')
            pProcedureCallStatement.exprList(self)
            print(' );', end='')


    def visitIIfStatement(self, iIfStatement):
        if iIfStatement != None:
            print('if ', end='')
            iIfStatement.expr_list(self)
            print(' then ', end='')
            iIfStatement.nstatement1(self)
            print(' else ', end='')
            iIfStatement.nstatement2(self)


    def visitWWhileStatement(self, wWhileStatement):
        if wWhileStatement != None:
            print('while ', end='')
            wWhileStatement.expr(self)
            print(' do')
            wWhileStatement.statement(self)


    def visitRRepeatStatement(self, rRepeatStatement):
        if rRepeatStatement != None:
            print('repeat ', end='')
            rRepeatStatement.statement(self)
            print(' until ', end='')
            rRepeatStatement.expr(self)
            print(';', end='')


    def visitFForStatement(self, fForStatement):
        if fForStatement != None:
            print('for ', end='')
            fForStatement.id(self)
            print(' := ', end='')
            fForStatement.expr1(self)
            print(' to ', end='')
            fForStatement.expr2(self)
            print(' do ', end='')
            fForStatement.statement(self)




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


    # p[0] = dict({p[1]: p[3]}.items() + p[0].items())
    # Gera um novo dicionário, inserindo os dados corretamente (organizado)