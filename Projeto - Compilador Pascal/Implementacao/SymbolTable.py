#Dicionario que representa a tabela de simbolos.
symbolTable = []
INTEGER = 'integer'
CONST = 'const'
REAL = 'real'
STRING = 'string'
BOOL = 'boolean'
TYPE = 'type'
PARAMS = 'params'
BINDABLE = 'bindable'
FUNCTION = 'fun'
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
    symbolTable[-1][name] = {BINDABLE: VARIABLE, TYPE : type}

def addConst(name, type):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: CONST, TYPE : type}

def addFunction(name, params, returnType):
    global symbolTable
    symbolTable[-1][name] = {BINDABLE: FUNCTION, PARAMS: params, TYPE : returnType}

def addProcedure(name, params):
    addFunction(name, params, None)

def getBindable(bindableName):
    global symbolTable
    for i in reversed(range(len(symbolTable))):
        if (bindableName in symbolTable[i].keys()):
            return symbolTable[i][bindableName]
    return None
