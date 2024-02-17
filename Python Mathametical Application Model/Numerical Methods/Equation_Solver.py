from parser_evaluater import *
import random
import sympy as sp


def find_root(equation, max_steps = 1000, root = random.randint(-10, 10)): 
    equation = parse(equation)
    diff = sp.diff(equation) 
    steps = 0
    value = 1
    while steps<=max_steps:
        value = evaluate_equation(equation, root)
        dv = evaluate_equation(diff, root)
        temp = root - (value/dv)
        #print(f"{root} - {value} / {dv}")
        root = temp
        steps += 1
        if value == 0:
            break
    return root
