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
           bBlock.subroutine_dec.accept(self)
        #bBlock.compoundStatement_dec.accept(self)




    def visitCConstDefinition(self, cConstDefinition):
        if cConstDefinition != None:
            print('const')
            for key in cConstDefinition.dicDefinicoes:
                print(key,' = ', cConstDefinition.dicDefinicoes[key], ';')




    def visitVVarDeclaration(self, vVarDeclaration):
        if vVarDeclaration != None:
            print('var')
            for key in vVarDeclaration.dicDefinicoes:
                print(key,' : ', vVarDeclaration.dicDefinicoes[key], ';')



    def visitPProcedureDeclaration(self, pProcedureDeclaration):
        if pProcedureDeclaration != None:
            for key in pProcedureDeclaration.dicDefinicoes:
                print('procedure', key, ' ( ', pProcedureDeclaration.dicDefinicoes[key], ' ) ;')


    def visitFFunctionDeclaration(self, fFunctionDeclaration):
        if fFunctionDeclaration != None:
            for key, v in fFunctionDeclaration.dicDefinicoes.items():
                print('function', fFunctionDeclaration.id, ' ( ', key, ' ) : ', v, ' ; ')
