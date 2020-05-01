# exp → exp + exp | exp - exp | exp * exp | exp / exp | exp ^ exp | log exp | call | assign | num | id
# call → id (params) | id ( )
# params → exp, params | exp
# assign → id = exp

import ply.yacc as yacc
from ExpressionLanguageLex import *
import SintaxeAbstrata as sa
import Visitor as vis


def p_exp_soma(p):
    '''exp : exp SOMA exp1
         | exp1'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = sa.SomaExp(p[1], p[3])


def p_exp1_vezes(p):
    '''exp1 : exp1 VEZES exp2
            | exp2'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = sa.MulExp(p[1], p[3])


def p_exp2_pot(p):
    '''exp2 : exp3 POT exp2
            | exp3'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = sa.PotExp(p[1], p[3])


def p_exp3_call(p):
    '''exp3 : call
            | assign
            | NUMBER
            | ID'''
    if isinstance(p[1], sa.Call):
        p[0] = sa.CallExp(p[1])
    elif isinstance(p[1], sa.Assign):
        p[0] = sa.AssignExp(p[1])
    elif isinstance(p[1], int):
        p[0] = sa.NumExp(p[1])
    else:
        p[0] = sa.IdExp(p[1])


def p_call_id_params(p):
    '''call : ID LPAREN params RPAREN
          | ID LPAREN RPAREN'''
    if len(p) == 5:
        p[0] = sa.ParamsCall(p[1], p[3])
    else:
        p[0] = sa.SimpleCall(p[1])


def p_params_ids(p):
    '''params : exp COMMA params
            | exp '''
    if len(p) == 2:
        p[0] = sa.SingleParam(p[1])
    elif len(p) == 4:
        p[0] = sa.CompoundParams(p[1], p[3])


def p_assign(p):
    '''assign : ID IGUAL exp'''
    p[0] = sa.AssignAss(p[1], p[3])


def p_error(p):
    print("Syntax error in input!")


lexer = lex.lex()
#
# # Test it out
data = '''
    b = 3
 '''
lexer.input(data)
parser = yacc.yacc()
result = parser.parse(debug=True)

visitor = vis.Visitor()
result.accept(visitor)


#a = chamada(a, b, 3 * 4)  + 3 * 8 ^ 25 + 144 + 31231 + andreSilva