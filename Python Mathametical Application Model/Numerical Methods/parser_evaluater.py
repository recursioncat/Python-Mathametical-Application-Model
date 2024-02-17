import math
import sympy as sp
import re

def evaluate_equation(equation, x_value):
    equation = str(equation)
    equation = equation.replace("^", "**").replace('e', '2.718281828459045')
    result = eval(equation, {'__builtins__': None}, {'x': x_value, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'sqrt': math.sqrt, 'log': math.log})
    return result


def lis_to_str(lis):
    result = ""
    for item in lis:
        result += item
    return result


def parse(equation):
    equation = change_signs(equation)
    equation = equation.lower()
    equation = equation.replace(" ", "").replace("+", " +").replace("-", " -").replace("x", "(x)")
    res_lis = []
    for exp in equation.split():
        if(exp[0].isdigit() or exp[0]=="+" or exp[0]=="-") and "x" in exp:
            for i, alpha in enumerate(exp):
                if alpha.isalpha() or alpha == "(":
                    result = exp[0:i]+"*"+exp[i:]
                    res_lis.append(result)
                    break
        else:
           res_lis.append(exp)
    return lis_to_str(res_lis)

def change_signs(equa):
    if "=" in equa:
        split=tokens=re.split(r"=", equa)
        if(split[1][0]!="-"):
            split[1]="+"+split[1]
        emp=""
        for items in split[1]:
            if(items!="+" and items!="-"):
                emp+=items
            elif(items=="+"):
                emp+="-"
            else:
                emp+="+"

        return (split[0]+emp)
    
    else :
        return equa

