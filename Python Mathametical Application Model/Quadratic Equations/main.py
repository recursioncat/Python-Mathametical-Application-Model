import math
import re

def process_division(eq):
    eq=eq.replace("(", "").replace(")", "")
    split2=re.split("/", eq)
    return float(int(split2[0])/int(split2[1]))

def change_signs(equa):
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

def process(var):
    var = var.replace(" ", "")  # remove =0 and then remove all spaces
    var = var.replace("X","x")
    # Add Spaces between each term
    sttr = ""
    for items in var:
        if items == "+":
            sttr += " +"
        elif items == "-":
            sttr += " -"
        else:
            sttr += items
    if sttr[0] != "-":
        sttr = "+" + sttr
    split = re.split(" ", sttr)
    for i in range(len((split))):
        if (split[i][1:] == "x^2") or (split[i][1:] == "x**2") or (split[i][1:] == "x") or (split[i][1:] == "x2"):
                split[i] = split[i][0] + "1" + split[i][1:]
    print(split)
            
    # Create an ultimate dictionary
    coeff = {"b": 0, "a": 0, "c": 0}
    for item in split:
        if (item.endswith("x^2") or item.endswith("x**2") or item.endswith("x2")):
            if("/" in item):
                var=process_division(re.split("x\^2|x\*\*2|x2", item)[0])
                coeff["a"] += var
            else:
                coeff["a"] += float(re.split("x\^2|x\*\*2|x2", item)[0])
        elif item.endswith("x"):
            if("/" in item):
                var=process_division(re.split("x", item)[0])
                coeff["b"] += var
            else:
                coeff["b"] += float(re.split("x", item)[0])
        else:
            if("/" in item):
                var=process_division(item)
                coeff["c"] += var
            else:
                coeff["c"] += float(item)

    return coeff
  
def quad(eq): #solves
    eq=change_signs(eq)
    coeff=process(eq)
    print(f"coeff:{coeff}")    
    delta = coeff["b"]**2 - 4*coeff["a"]*coeff["c"]
    if delta < 0:
        print("There are no real roots.")
        return None
    elif delta == 0:
        sol1 = -coeff["b"] / (2*coeff["a"])
        print(f"The only real root is {sol1}")
        return [sol1]
    else:
        sol1 = (-coeff["b"] + math.sqrt(delta)) / (2*coeff["a"])
        sol2 = (-coeff["b"] - math.sqrt(delta)) / (2*coeff["a"])
        print(f"The two real roots are {sol1} and {sol2}")
        return [sol1,sol2]
