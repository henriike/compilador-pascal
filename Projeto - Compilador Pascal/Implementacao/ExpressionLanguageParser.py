# -------------------------
# ExpressionLanguageParser.py
#----------------------

import os
import ply.yacc as yacc
from ExpressionLanguageLex import *
import SintaxeAbstrata as sa
import Visitor as vis
import SemanticVisitor as sv


precedence = (
    # Operadores relacionais (=, <, <=, >, >=, <>)
    ('nonassoc', 'EQUALS', 'LTHAN', 'LEQUALS', 'GTHAN', 'GEQUALS', 'DIFFERENT'),

    # Operadores Aditivos
    ('left', 'PLUS', 'MINUS', 'OR'),

    # Operadores Multiplicativos (*, /, div, MOD)
    ('left', 'TIMES', 'DIVIDE', 'DIV', 'MOD', 'AND'),

    # Operadores Unários (+, -) --> Possuem maior precedência entre os aritméticos
    ('left', 'UMINUS', 'UPLUS'),

    # O operador NOT é associativo a direita
    ('right', 'NOT')

    # Operador Parêntesis
    # ('left', 'LPARENT', 'RPARENT')
)


# Declaração do program que pode encadear na declaração de blocos
def p_program(p):
    '''
    program : PROGRAM ID SEMICOLON block
            | PROGRAM ID SEMICOLON
    '''
    if len(p) == 4:
        p[0] = sa.PProgram(p[2], None)
    else:
        p[0] = sa.PProgram(p[2], p[4])



# Declaração dos blocos
def p_block(p):
    '''
    block : const_declaration_part var_declaration_part subroutine_declaration_part compound_statement_score
    '''
    p[0] = sa.BBlock(p[1], p[2], p[3], p[4])



# Declaração de constantes
def p_const_declaration_part(p):
    '''
    const_declaration_part : CONST const_definition
                           |          
    '''
    if len(p) == 1:
        p[0] = None
    else:
        p[0] = p[2]

def p_const_definition(p):
    '''
    const_definition : ID EQUALS types SEMICOLON const_definition
                    |  ID EQUALS types SEMICOLON
    '''
    if len(p) == 5:
        p[0] = sa.CConstDefinition({})
        p[0].dicDefinicoes.update({p[1]: p[3]})
    else:
        p[5].dicDefinicoes.update({p[1]: p[3]})
        p[0] = p[5]




# Declaração de variáveis
def p_var_declaration_part(p):
    '''
    var_declaration_part : VAR var_declaration
                         |
    '''
    if len(p) == 1:
        p[0] = None
    else:
        p[0] = p[2]

def p_var_declaration(p):
    '''
    var_declaration : identifier_list TWOPOINTS types SEMICOLON var_declaration
                    | identifier_list TWOPOINTS types SEMICOLON
    '''
    if len(p) == 5:
        p[0] = sa.VVarDeclaration({})
        p[0].dicDefinicoes.update({p[1]: p[3]})
    else:
        p[5].dicDefinicoes.update({p[1]: p[3]})
        p[0] = p[5]

# Tipos de dados
def p_types(p):
    '''
    types : INTEGER
          | REAL
          | STRING
          | BOOLEAN
          | CHAR
          | ID
    '''
    p[0] = p[1]


# Repetição de variáveis
def p_identifier_list(p):
    '''
    identifier_list : ID
                    | ID COMMA identifier_list
    '''

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + " , " + str(p[3])



# Subroutine chama procedure ou function
def p_subroutine_declaration_part(p):
    '''
    subroutine_declaration_part : procedure_declaration subroutine_declaration_part
                                | function_declaration subroutine_declaration_part
                                |
    '''
    if len(p) == 1:
        p[0] = []
    else:
        p[2].insert(0, p[1])
        p[0] = p[2]


# Declaração de procedimento -> Funções que não retornam valor
def p_procedure_declaration(p):
    '''
    procedure_declaration : PROCEDURE ID LPARENT param_section RPARENT SEMICOLON
    '''

    p[0] = sa.PProcedureDeclaration({})
    p[0].dicDefinicoes.update({p[2]:p[4]})


# Declaração de função -> Funções que retornam valor
def p_function_declaration(p):
    '''
    function_declaration : FUNCTION ID LPARENT param_section RPARENT TWOPOINTS types SEMICOLON
    '''
    p[0] = sa.FFunctionDeclaration({}, p[2])
    p[0].dicDefinicoes.update({p[4]:p[7]})


# Declaração de parâmetros das funções
def p_param_section(p):
    '''
    param_section : identifier_list TWOPOINTS types SEMICOLON param_section
                  |
    '''
    if len(p) == 1:
        p[0] = ''
    else:
        p[0] = str(p[1]) + " : " + p[3] + " ; " + str(p[5])



# Declaração do compound_statement que chama o statement, onde o statement
# engloba: assign, procedure_call, if, case, while, repeat, for

def p_compound_statement_score(p):
    '''
    compound_statement_score : BEGIN statements END SCORE
                             | BEGIN END SCORE
    '''
    if len(p) == 5:
        p[0] = p[2]



def p_compound_statement_semicolon(p):
    '''
    compound_statement_semicolon : BEGIN statements END SEMICOLON
                                 | BEGIN END SEMICOLON
    '''
    if len(p) == 5:
        p[0] = sa.CCompoundStatementSemicolon(p[2])


def p_statements(p):
    '''
    statements : statement
               | statement statements
    '''
    if len(p) == 2:
        p[0] = sa.SSingleStatement(p[1])
    else:
        p[0] = sa.CCompoundStatement(p[1], p[2])


def p_statement(p):
    '''
    statement : nstatement
              | if2_statement
    '''
    p[0] = p[1]


def p_nstatement(p):
    '''
    nstatement : assign_statement
               | procedure_call_statement
               | IF LPARENT expr_list RPARENT THEN nstatement ELSE nstatement
               | case_statement
               | while_statement
               | repeat_statement
               | for_statement
               | compound_statement_semicolon
    '''
    if p[1] == 'if':
        p[0] = sa.IIfStatement(p[3], p[6], p[8])
    else:
        p[0] = p[1]




# Atribuição
def p_assign_statement(p):
    '''
    assign_statement : ID ASSIGNMENT expr SEMICOLON
    '''
    p[0] = sa.AAssignStatement(p[1], p[3])


# Chamada de função
def p_procedure_call_statement(p):
    '''
    procedure_call_statement :  ID LPARENT expr_list RPARENT SEMICOLON
    '''
    p[0] = sa.PProcedureCallStatement(p[1], p[3])


def p_if2_statement(p):
    '''
    if2_statement : IF LPARENT expr_list RPARENT THEN statement
                  | IF LPARENT expr_list RPARENT THEN nstatement ELSE if2_statement
    '''
    if len(p) == 7:
        p[0] = sa.IIfStatement(p[3], p[6], None)
    else:
        p[0] = sa.IIfStatement(p[3], p[6], p[8])


# Estrutura de Repetição - While
def p_while_statement(p):
    '''
    while_statement : WHILE expr DO statement
    '''
    p[0] = sa.WWhileStatement(p[2], p[4])


# Estrutura de Repetição - Repeat
def p_repeat_statement(p):
    '''
    repeat_statement : REPEAT statement UNTIL expr SEMICOLON
    '''
    p[0] = sa.RRepeatStatement(p[2], p[4])



# Estrutura de Repetição - For
# No caso To é usado, se o valor inicial for maior que o valor final, a instrução nunca será executada.
# No caso de DownTo ser usado, se o valor inicial for menor que o valor final, a instrução nunca será executada.
def p_for_statement(p):
    '''
    for_statement : FOR ID ASSIGNMENT expr TO expr DO statement
    '''
    p[0] = sa.FForStatement(p[2], p[4], p[6], p[8])



# Estrutura CASE - SWITCH
def p_case_statement(p):
    '''
    case_statement : CASE expr OF cases END SEMICOLON
    '''
    p[0] = sa.CCaseStatement(p[2], p[4])


def p_cases(p):
    '''
    cases : case
          | case cases
    '''
    if len(p) == 2:
        p[0] = sa.SSingleCase(p[1])
    else:
        p[0] = sa.CCompoundCase(p[1], p[2])


def p_case(p):
    '''
    case : INTEGER TWOPOINTS statement
         | REAL TWOPOINTS statement
         | ID TWOPOINTS statement
    '''
    if isinstance(p[1], int):
        p[0] = sa.IIntegerCase(p[1], p[3])
    elif isinstance(p[1], float):
        p[0] = sa.RRealCase(p[1], p[3])
    else:
        p[0] = sa.IIdCase(p[1], p[3])



# Declaração de expr_list
def p_expr_list(p):
    '''
    expr_list : expr
              | expr COMMA expr_list
    '''
    if len(p) == 2:
        p[0] = sa.SSingleExprList(p[1])
    else:
        p[0] = sa.CCompoundExprList(p[1], p[3])


def p_expr(p):
    '''
    expr :  expr EQUALS expr
          | expr LTHAN expr
          | expr GTHAN expr
          | expr DIFFERENT expr
          | expr GEQUALS expr
          | expr LEQUALS expr
          | expr PLUS expr
          | expr MINUS expr
          | expr OR expr
          | expr TIMES expr
          | expr DIVIDE expr
          | expr DIV expr
          | expr MOD expr
          | expr AND expr
          | PLUS expr %prec UPLUS
          | MINUS expr %prec UMINUS
          | factor
    '''
    if len(p) == 4:
        if p[2] == '=':
            p[0] = sa.EEqualsExp(p[1], p[3])
        elif p[2] == '<':
            p[0] = sa.LLthanExp(p[1], p[3])
        elif p[2] == '>':
            p[0] = sa.GGthanExp(p[1], p[3])
        elif p[2] == '<>':
            p[0] = sa.DDifferentExp(p[1], p[3])
        elif p[2] == '>=':
            p[0] = sa.GGequals(p[1], p[3])
        elif p[2] == '<=':
            p[0] = sa.LLequalsExp(p[1], p[3])
        elif p[2] == '+':
            p[0] = sa.PPlusExp(p[1], p[3])
        elif p[2] == '-':
            p[0] = sa.MMinusExp(p[1], p[3])
        elif p[2] == 'or':
            p[0] = sa.OOrExp(p[1], p[3])
        elif p[2] == '*':
            p[0] = sa.TTimesExp(p[1], p[3])
        elif p[2] == '/':
            p[0] = sa.DDivideExp(p[1], p[3])
        elif p[2] == 'div':
            p[0] = sa.DDivExp(p[1], p[3])
        elif p[2] == 'mod':
            p[0] = sa.MModExp(p[1], p[3])
        elif p[2] == 'and':
            p[0] = sa.AAndExp(p[1], p[3])

    elif len(p) == 3:
        if p[1] == '+':
            p[0] = sa.UPPlusExp(p[2])
        elif p[1] == '-':
            p[0] = sa.UMMinusExp(p[2])

    else:
        p[0] = p[1]




def p_factor(p):
    '''
    factor : ID
           | INTEGER
           | REAL
           | STRING
           | TRUE
           | FALSE
           | NOT factor
    '''
    if len(p) == 2:
        if isinstance(p[1], int):
            p[0] = sa.FFactorInt(p[1])
        elif isinstance(p[1], float):
            p[0] = sa.FFactorReal(p[1])
        elif p[1][0] == '\'':
            p[0] = sa.FFactorString(p[1])
        elif p[1] == 'true' or p[1] == 'false':
            p[0] = sa.FFactorBoolean(p[1])
        else:
            p[0] = sa.FFactorId(p[1])
    else:
        p[0] = sa.FFactorNot(p[2])








def p_error(p):
    print("Syntax error in input!")



# Ler arquivo.pas para ser compilado
# cwd = os.getcwd() + "\Implementacao\codigoFontePascal\codigo.txt";
arquivo = open('codigo.txt','r')
codigo = arquivo.read()
arquivo.close()


lexer = lex.lex()

## Test it out
data = codigo

 
lexer.input(data)
parser = yacc.yacc()
result = parser.parse(debug=False)


visitor = sv.SemanticVisitor()
#visitor = vis.Visitor()
result.accept(visitor)




