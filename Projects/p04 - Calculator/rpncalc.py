"""Reverse Polish calculator.

This RPN calculator creates an expression tree from
the input.  It prints the expression in algebraic
notation and then prints the result of evaluating it.
"""
'''Owen Ferguson, CS211 2-5-2024'''

import lex
from expr import *
import io

def env_clear():
    """Clear all variables in calculator memory"""
    global ENV
    ENV = dict()

BINOPS = { lex.TokenCat.PLUS : Plus,
           lex.TokenCat.TIMES: Times,
           lex.TokenCat.DIV: Div,
           lex.TokenCat.MINUS:  Minus
        }

def rpn_parse(text: str) -> list[Expr]:
    """Parse text in reverse Polish notation
    into a list of expressions (exactly one if
    the expression is balanced).
    Example:
        rpn_parse("5 3 + 4 * 7")
          => [ Times(Plus(IntConst(5), IntConst(3)), IntConst(4)))),
               IntConst(7) ]
    May raise:  ValueError for lexical or syntactic error in input 
    """
    tokens = text.split()
    tokens2 = lex.TokenStream(io.StringIO(text))
    stack = []
    for token in tokens:
        tok = tokens2.take()
        if token.isdigit():
            stack.append(IntConst(int(token)))

        elif token in ('+', '-', '*', '/'):
            if len(stack) < 2:
                raise ValueError("Not enough operands for operator")
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.append(Plus(left, right))
            elif token == '-':
                stack.append(Minus(left, right))
            elif token == '*':
                stack.append(Times(left, right))
            elif token == '/':
                stack.append(Div(left, right))
    
        elif tok.kind == lex.TokenCat.ASSIGN:
            right = stack.pop()
            left = stack.pop()
            stack.append(Assign(right, left))
    
        elif token.isalpha():  # Check if token is a variable
            stack.append(Var(token))

        else:
            raise ValueError("Invalid token")

    if len(stack) != 1:
        raise ValueError("Invalid expression")
    return stack

def calc(text: str):
    """Read and evaluate a single line formula."""
    try:
        stack = rpn_parse(text)
        if len(stack) == 0:
            print("(No expression)")
        else:
            # For a balanced expression there will be one Expr object
            # on the stack, but if there are more we'll just print
            # each of them
            for exp in stack:
                print(f"{exp} => {exp.eval()}")
    except Exception as e: 
        print(e)

def rpn_calc():
    txt = input("Expression (return to quit):")
    while len(txt.strip()) > 0:
        if txt.isalpha():  # Check if input is a single variable
            # Print the variable's value if it exists in the environment
            if txt in ENV:
                print(f"{txt} = {ENV[txt]}")
            else:
                print(f"Variable '{txt}' is not defined")
        else:
            calc(txt)
        txt = input("Expression (return to quit):")
    print("Bye! Thanks for the math!")



if __name__ == "__main__":
    """RPN Calculator as main program"""
    rpn_calc()






