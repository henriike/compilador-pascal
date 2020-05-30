# -------------------------
# ExpressionLanguageLex.py
#----------------------

#coding: utf-8

import ply.lex as lex 
import re

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
    'procedure' : 'PROCEDURE',
    'program'   : 'PROGRAM',
    'until'     : 'UNTIL',
    'repeat'    : 'REPEAT',
    'while'     : 'WHILE',
    'to'        : 'TO',
    'of'        : 'OF',
    'var'       : 'VAR',
    'integer'   : 'INTEGER',
    'real'      : 'REAL',
    'string'    : 'STRING',
    'char'      : 'CHAR',
    'boolean'   : 'BOOLEAN',
    'exp'       : 'EXP',
    'true'      : 'TRUE',
    'false'     : 'FALSE',
}

 # Lista de nomes de tokens. Isso é sempre necessário
tokens = [
    'COMMENT',
    'PLUS', 
    'MINUS', 
    'TIMES', 
    'DIVIDE',
    'DIVIDE_INT',
    'EQUALS',
    'ASSIGNMENT',
    'DIFFERENT',
    'LEQUALS',
    'GEQUALS',
    'LTHAN',
    'GTHAN',
    'RESERVED',
    'ID',
    'LBRACKET',
    'RBRACKET',
    'LPARENT',
    'RPARENT',
    'SCORE',
    'COMMA',
    'TWOPOINTS',
    'SEMICOLON',
    'UMINUS',
    'UPLUS'
] + list(reserved.values())


# Operators Unary (+, -)
#t_UMINUS = r'\-'
#t_UPLUS = r'\+'

# Arithmetic Operators ( + - * / %)
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'


# Relational Operators ( := < <= > >= = <> )
t_ASSIGNMENT = r':='
t_LTHAN = r'<'
t_LEQUALS = r'<='
t_GTHAN = r'>'
t_GEQUALS = r'>='
t_EQUALS = r'='
t_DIFFERENT = r'<>'


# Delimeters
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r']'
t_SCORE = r'\.'
t_COMMA = r'\,'
t_SEMICOLON = r';'
t_TWOPOINTS = r'\:'



# Define uma regra para rastrear nomes de variáveis ID (OK!)
def t_ID(t):
    r'([0-9]?\d*[a-zA-Z_][a-zA-Z_0-9]*)'
    t.type = reserved.get(t.value.lower(),'ID')    # Check for reserved words
    
    if len(t.value) <= 255:
        return t

# Define uma regra para rastrear palavras reservadas (OK!)

# --------------------IMPORTANTE -------------------------
# Por íncrivel que pareça, colocar a regra do float antes da regra do integer funciona a regex de cada uma (rastrear número inteiro e 
# rastrear número float), regex essas que se inverter a ordem das regras colocando a regra integer acima da regra do float as regex
# que funcionavam na outra ordem já não funcionam mais...

# Define uma regra para rastrear números float (OK!)
def t_REAL(t):
    r'[-]?\d+[.]\d+'
    t.value = float(t.value)
    return t

# Define uma regra para rastrear números inteiros (OK!)
def t_INTEGER(t):
    r'[-]?\d+'
    t.value = int(t.value)
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

def t_CHAR(t):
    r'\'\w\''
    return t

# Define uma regra para que possamos rastrear números de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Uma sequência contendo caracteres ignorados (espaços e tabulações)    
t_ignore = ' \t'

# Regra de tratamento de erros
def t_error(t):
   print("Illegal character '%s'" % t.value[0])
   t.lexer.skip(1)
