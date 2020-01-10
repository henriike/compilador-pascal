#coding: utf-8

import ply.lex as lex 
import re
import stack

# Define um conjunto com todas as palavras reservadas
reserved = {
    'array'     : 'ARRAY',
    'begin'     : 'BEGIN',
    'case'      : 'CASE',
    'const'     : 'CONST',
    'div'       : 'DIV',
    'do'        : 'DO',
    'downto'    : 'DOWNTO',
    'else'      : 'ELSE',
    'end'       : 'END',
    'for'       : 'FOR',
    'function'  : 'FUNCTION',
    'mod'       : 'MOD',
    'if'        : 'IF',
    'then'      : 'THEN',
    'and'       : 'AND',
    'or'        : 'OR',
    'not'       : 'NOT',
    'xor'       : 'XOR',
    'procedure' : 'PROCEDURE',
    'program'   : 'PROGRAM',
    'until'     : 'UNTIL',
    'repeat'    : 'REPEAT',
    'var'       : 'VAR',
    'nil'       : 'NIL',
    'shr'       : 'SHR',
    'shl'       : 'SHL',
    'while'     : 'WHILE',
    'with'      : 'WITH',
    'to'        : 'TO',
    'of'        : 'OF'
}

 # Lista de nomes de tokens. Isso é sempre necessário
tokens = [
    'COMMENT',
    'CONST_INT',
    'CONST_FLOAT',
    'BOOLEAN',
    'STRING',
    'PLUS', 
    'MINUS', 
    'TIMES', 
    'DIVIDE',
    'EQUALS',
    'DIFFERENT',
    'LEQUALS',
    'GEQUALS',
    'LTHAN',
    'GTHAN',
    'RESERVED',
    'ID',
    'LEFTBRACKET',
    'RIGHTBRACKET',
    'LEFTPARENTHESES',
    'RIGHTPARENTHESES',
    'SCORE',
    'COMMA',
    'TWOPOINTS',
    'CIRCUMFLEX',

] + list(reserved.values())

# Regras de expressão regular para tokens simples
t_ignore = ' \t' # Uma sequência contendo caracteres ignorados (espaços e tabulações)
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_DIFFERENT = r'<>'
t_LEQUALS = r'<='
t_GEQUALS = r'>='
t_LTHAN = r'<'
t_GTHAN = r'>'
t_LEFTBRACKET = r'\['
t_RIGHTBRACKET = r']'
t_LEFTPARENTHESES = r'\('
t_RIGHTPARENTHESES = r'\)'
t_SCORE = r'\.'
t_COMMA = r'\,'
t_TWOPOINTS = r'\:'
t_CIRCUMFLEX = r'\^'


# Define uma regra para rastrear nomes de variáveis ID (OK!)
def t_ID(t):
    r'([0-9]?\d*[a-zA-Z_][áãíéêôáâa-zA-Z_0-9]*)'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    if len(t.value) <= 255:

        if (t.value[0].isnumeric() or 'á' in t.value or "ã" in t.value or "í" in t.value or "é" in t.value or "ê" in t.value or "ô" in t.value or "â" in t.value):
            print("Token invalido -- " + t.value)
        else:    
            return t

    else: 
        print("Nome de identificador inválido!")

# Define uma regra para rastrear palavras reservadas (OK!)
def t_RESERVED(t):
     r'(?!true)(?!false)[a-zA-Z_][a-zA-Z_0-9]*'
     t.type = reserved.get(t.value,(t.value))    # Check for reserved words
     return t

# --------------------IMPORTANTE -------------------------
# Por íncrivel que pareça, colocar a regra do float antes da regra do integer funciona a regex de cada uma (rastrear número inteiro e 
# rastrear número float), regex essas que se inverter a ordem das regras colocando a regra integer acima da regra do float as regex
# que funcionavam na outra ordem já não funcionam mais...

# Define uma regra para rastrear números float (OK!)
def t_CONST_FLOAT(t):
    r'[-]?\d+[.]\d+'
    t.value = float(t.value)
    return t

# Define uma regra para rastrear números inteiros (OK!)
def t_CONST_INT(t):
    r'[-]?\d+'
    t.value = int(t.value)
    return t

# Define uma regra para rastrear valores booleanos (OK!)
def t_BOOLEAN(t):
    r'true+|false+'
    t.value = str(t.value)
    t.value = t.value.replace("'", "")
    return t

# Define uma regra para rastrear comentários (OK!) {} (**) //
def t_COMMENT(t):
    r'(({)[\w\d !@#$%¨&*()_+^~?\'"/*-+.,<>|ºª`//]*(})) | \/\/.* |  \(\* ([\w\d  !@#$%¨&_+^~?\'"/*-+.,<>|ºª`//]*) \*\) '
    t.value = str(t.value)
    t.value = t.value.replace("\"","")
    pass 

# Define uma regra para que possamos rastrear strings (OK!)
def t_STRING(t):
    r'\'[\w\d !@#$%¨&*()_+^~?\"/*-+.,<>|ºª`//]* \' '
    #r'((\')[\w\d !@#$%¨&*()_+^~?\'"/*-+.,<>|ºª`//]*(\'))'
    t.value = str(t.value)
    t.value = t.value.replace("'","")
    return t

# Define uma regra para que possamos rastrear números de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Ler arquivo
arquivo = open('AnalisadorLexico\cod.txt','r')
codigo = arquivo.read()
arquivo.close()

# Regra de tratamento de erros
def t_error (t):
     print ("Caractere ilegal '% s'"% t.value [0])
     t.lexer.skip (1)

# Construa o lexer
lexer = lex.lex()

# Dê ao lexer alguma contribuição
lexer.input(codigo)

# Tokenize
while True:
     tok = lexer.token()
     if not tok: 
         break      # No more input
     print(tok)