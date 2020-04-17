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



    def visitEExpressao(self, eExpressao):
        for key in eExpressao.dicDefinicoes.keys():
            print(key, eExpressao.dicDefinicoes[key])



    # p[0] = dict({p[1]: p[3]}.items() + p[0].items())
    # Gera um novo dicionário, inserindo os dados corretamente (organizado)