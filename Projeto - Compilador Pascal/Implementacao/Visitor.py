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
            # Introduzimos o accept
            cCompoundStatementScore.statements.accept(self)
            print('end.', end='')



    # Visitor do CompoundStatementSemicolon

    def visitCCompoundStatementSemicolon(self, cCompoundStatementSemicolon):
        if cCompoundStatementSemicolon != None:
            print('begin', end='')
            cCompoundStatementSemicolon.statements.accept(self)
            print('end;', end='')



    # Visitor do Statements

    def visitSSingleStatement(self, sSingleStatement):
        if sSingleStatement != None:
            sSingleStatement.statementt.accept(self)

    def visitCCompoundStatement(self, cCompoundStatement):
        if cCompoundStatement != None:
            cCompoundStatement.statementt.accept(self)
            print(' ', end='')
            cCompoundStatement.statementss.accept(self)



    # Visitor do Statement

    def visitAAssignStatement(self, aAssignStatement):
        if aAssignStatement != None:
            print(aAssignStatement.id, ':= ', end='')
            aAssignStatement.exp.accept(self)
            print(';')


    def visitPProcedureCallStatement(self, pProcedureCallStatement):
        if pProcedureCallStatement != None:
            print(pProcedureCallStatement.id, '( ', end='')
            pProcedureCallStatement.exprList.accept(self)
            print(' );')


    def visitWWhileStatement(self, wWhileStatement):
        if wWhileStatement != None:
            print('while ', end='')
            wWhileStatement.expr.accept(self)
            print(' do')
            wWhileStatement.statement.accept(self)


    def visitRRepeatStatement(self, rRepeatStatement):
        if rRepeatStatement != None:
            print('repeat ', end='')
            rRepeatStatement.statement.accept(self)
            print(' until ', end='')
            rRepeatStatement.expr.accept(self)
            print(';', end='')


    def visitFForStatement(self, fForStatement):
        if fForStatement != None:
            print('for ', fForStatement.id, ':=', end='')
            fForStatement.expr1.accept(self)
            print(' to ', end='')
            fForStatement.expr2.accept(self)
            print(' do ', end='')
            fForStatement.statement.accept(self)



    def visitCCaseStatement(self, cCaseStatement):
        if cCaseStatement != None:
            print('case ', end='')
            cCaseStatement.expr.accept(self)
            print(' of')
            cCaseStatement.cases.accept(self)
            print('end;')

    def visitSSingleCase(self, sSingleCase):
        if sSingleCase != None:
            sSingleCase.case.accept(self)

    def visitCCompoundCase(self, cCompoundCase):
        if cCompoundCase != None:
            cCompoundCase.case.accept(self)
            print(' ', end='')
            cCompoundCase.cases.accept(self)

    def visitIIntegerCase(self, iIntegerCase):
        if iIntegerCase != None:
            print(iIntegerCase.token, ' : ', end='')
            iIntegerCase.statement.accept(self)

    def visitRRealCase(self, rRealCase):
        if rRealCase != None:
            print(rRealCase.token, ' : ', end='')
            rRealCase.statement.accept(self)

    def visitIIdCase(self, iIdCase):
        if iIdCase != None:
            print(iIdCase.token, ' : ', end='')
            iIdCase.statement.accept(self)


    def visitIIfStatement(self, iIfStatement):
        if iIfStatement != None:
            print('if (', end='')
            iIfStatement.expr_list.accept(self)
            print(') then ', end='')
            iIfStatement.nstatement1.accept(self)

            if iIfStatement.nstatement2 != None:
                print(' else ', end='')
                iIfStatement.nstatement2.accept(self)

    # Visitor do ExprList

    def visitSSingleExprList(self, sSingleExprList):
        sSingleExprList.expr.accept(self)

    def visitCCompoundExprList(self, cCompoundExprList):
        cCompoundExprList.expr1.accept(self)
        print(' , ', end='')
        cCompoundExprList.expr2.accept(self)



    # Visitor das Expressões

    def visitEEqualsExp(self, eEqualsExp):
        eEqualsExp.exp1.accept(self)
        print(' = ', end='')
        eEqualsExp.exp2.accept(self)

    def visitLLthanExp(self, lLthanExp):
        lLthanExp.exp1.accept(self)
        print(' < ', end='')
        lLthanExp.exp2.accept(self)

    def visitGGthanExp(self, gGthanExp):
        gGthanExp.exp1.accept(self)
        print(' > ', end='')
        gGthanExp.exp2.accept(self)

    def visitDDifferentExp(self, dDifferentExp):
        dDifferentExp.exp1.accept(self)
        print(' <> ', end='')
        dDifferentExp.exp2.accept(self)

    def visitGGequals(self, gGequals):
        gGequals.exp1.accept(self)
        print(' >= ', end='')
        gGequals.exp2.accept(self)

    def visitLLequalsExp(self, lLequalsExp):
        lLequalsExp.exp1.accept(self)
        print(' <= ', end='')
        lLequalsExp.exp2.accept(self)

    def visitPPlusExp(self, pPlusExp):
        pPlusExp.exp1.accept(self)
        print(' + ', end='')
        pPlusExp.exp2.accept(self)

    def visitMMinusExp(self, mMinusExp):
        mMinusExp.exp1.accept(self)
        print(' - ', end='')
        mMinusExp.exp2.accept(self)

    def visitOOrExp(self, oOrExp):
        oOrExp.exp1.accept(self)
        print(' or ', end='')
        oOrExp.exp2.accept(self)

    def visitTTimesExp(self, tTimesExp):
        tTimesExp.exp1.accept(self)
        print(' * ', end='')
        tTimesExp.exp2.accept(self)

    def visitDDivideExp(self, dDivideExp):
        dDivideExp.exp1.accept(self)
        print(' / ', end='')
        dDivideExp.exp2.accept(self)

    def visitDDivExp(self, dDivExp):
        dDivExp.exp1.accept(self)
        print(' div ', end='')
        dDivExp.exp2.accept(self)

    def visitMModExp(self, mModExp):
        mModExp.exp1.accept(self)
        print(' mod ', end='')
        mModExp.exp2.accept(self)

    def visitAAndExp(self, aAndExp):
        aAndExp.exp1.accept(self)
        print(' and ', end='')
        aAndExp.exp2.accept(self)

    def visitUPPlusExp(self, uPPlusExp):
        print('+', end='')
        uPPlusExp.exp.accept(self)

    def visitUMMinusExp(self, uMMinusExp):
        print('-', end='')
        uMMinusExp.exp.accept(self)


    # Visitor do Factor

    def visitFFactorString(self, fFactorString):
        print(fFactorString.literal, end='')

    def visitFFactorInt(self, fFactorInt):
        print(fFactorInt.literal, end='')

    def visitFFactorReal(self, fFactorReal):
        print(fFactorReal.literal, end='')

    def visitFFactorId(self, fFactorId):
        print(fFactorId.literal, end='')

    def visitFFactorBoolean(self, fFactorBoolean):
        print(fFactorBoolean.literal, end='')

    def visitFFactorNot(self, fFactorNot):
        print(' not ', fFactorNot.literal, end='')


    # p[0] = dict({p[1]: p[3]}.items() + p[0].items())
    # Gera um novo dicionário, inserindo os dados corretamente (organizado)