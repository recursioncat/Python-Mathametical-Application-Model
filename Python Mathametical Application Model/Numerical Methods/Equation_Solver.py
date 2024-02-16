from temp import *
import random
import sympy as sp

equation = input("Enter Equation: ")
de = str(sp.diff(equation,  "x")).replace("*", "").replace(" ","")
if "x+" not in de or "x-" not in de:
    de = de.replace("x", "x^")
if  "+x" not in de or "-x" not in de:
    de = de.replace("x", "*x")

max_steps = 1000
some_number = random.randint(-10, 10)


steps = 0
value = 1
while steps<=max_steps:
    value = evaluate_equation(equation, some_number)
    dv = evaluate_equation(de, some_number)
    temp = some_number - (value/dv)
    some_number = temp
    steps += 1
    if value == 0:
        break

print(some_number)


# fix parsing issues