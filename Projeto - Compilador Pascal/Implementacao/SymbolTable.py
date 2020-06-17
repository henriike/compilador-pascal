#Dicionario que representa a tabela de simbolos.
symbolTable = []
INTEGER = 'integer'
CONST = 'const'
REAL = 'real'
STRING = 'string'
CHAR = 'char'
BOOL = 'boolean'
TYPE = 'type'
PARAMS = 'params'
BINDABLE = 'bindable'
FUNCTION = 'function'
PROCEDURE = 'procedure'
VARIABLE = 'var'
SCOPE = 'scope'
Number = [INTEGER, REAL]


def beginScope(nameScope):
    global symbolTable
    symbolTable.append({})
    symbolTable[-1][SCOPE] = nameScope

def endScope():
    global symbolTable
    symbolTable = symbolTable[0:-1]


def addVar(name, type):
    global symbolTable

    # Verifica se tem algum parâmetro separado por vírgula
    if ',' in name:

        # Existindo parâmetros separados por vírgula
        # Faz uma lista desses parâmetros utilizando como base a vírgula
        temp = name.split(",")

        for var in temp:
            # Esse var recebe cada linha que tem mais de 1 parâmetro
            # Tira o espaço de cada elemento, sem isso na tabela de símbolos eles ficam assim: 'expoente 1
            # Portanto de alguma forma não será reconhecido e receberá o valor None
            var = var.replace(" ", "")

            #Adiciona de fato na tabela de símbolos
            symbolTable[-1][var] = {BINDABLE: VARIABLE, TYPE: type}

    else:
        symbolTable[-1][name] = {BINDABLE: VARIABLE, TYPE: type}




def addConst(name, type):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: CONST, TYPE : type}

def addFunction(name, params, returnType):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: FUNCTION, PARAMS: params, TYPE : returnType}

def addProcedure(name, params):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: PROCEDURE, PARAMS: params}

'''
def addProcedure(name, params):
    addFunction(name, params, None)
'''

def getBindable(bindableName):
    global symbolTable
    for i in reversed(range(len(symbolTable))):
        if (bindableName in symbolTable[i].keys()):
            return symbolTable[i][bindableName]
    return None
