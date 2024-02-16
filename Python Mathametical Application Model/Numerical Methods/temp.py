import math
import sympy as sp

def evaluate_equation(equation, x_value):
    equation = equation.replace('sinx', 'sin(x)').replace("^", "**").replace('e', '2.718281828459045')
    result = eval(equation, {'__builtins__': None}, {'x': x_value, 'sin': math.sin, 'cos': math.cos, 'tan': math.tan, 'sqrt': math.sqrt, 'log': math.log})
    return result


def find_derivative(equation, variable='x'):
    x = sp.symbols(variable)
    try:
        equation = equation.replace(" ", "")
        if "+x" not in equation:
            equation = equation.replace("x", "*x")
        expr = sp.parse_expr(equation.replace("^", "**"))  # Replace '^' with '**'
        derivative = sp.diff(expr, x)
        return str(derivative).replace("*", "")
    except sp.SympifyError as e:
        return f"Error: {e}"

if __name__ == "__main__":
    derivative = str(sp.diff("x**3 - 3*x - 5",  "x")).replace("*", "")
    print(derivative)


