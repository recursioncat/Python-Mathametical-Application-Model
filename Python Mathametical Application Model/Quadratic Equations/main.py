import re
import math

def arrange_eq(var):   
    var=var.replace(" ", "")
    sttr=""
    for items in var:
        if(items=="+"):
            sttr+=" +"
        elif(items=="-"):
            sttr+=" -"
        else:
            sttr+=items
    sttr = sttr[:-2]
    if(sttr[0]!="-"):
        sttr="+"+sttr

    lst=["", "", ""]
    split=sttr.split()

    for item in split:
        if item.endswith("x**2"):
            lst[0]=item
        elif item.endswith("x"):
            lst[1]=item
        else:
            lst[2]=item

    return (lst_to_str(lst)+"=0")

def add_zeros(var):
    split=re.split("=",var)
    split2=re.split("[+|-]", split[0])
    count=0
    for item in split2:
        if(item.endswith("x")):
            count=1
    if(count==0):
        var="0x+"+var
        return var
    else:
        return var

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

    return (split[0]+emp+"=0")

def eq_split(eq): #takes what it needs
    
    split=re.split(r"=", eq)
    if(split[1]!="0"):
        eq=change_signs(eq)
        
    print(eq)
    eq=add_zeros(eq)
    print(eq)
    eq=arrange_eq(eq)
    print(eq)
    
    tokens=re.split(r"x\*\*2|x|=", eq)
    while("" in tokens):
        tokens.remove("")
    coeff={}
    
    try:
        coeff["a"] = eval(tokens[0])
    except:
        coeff["a"] = 1
        
    try:
        coeff["b"] = eval(tokens[1])
    except:
        coeff["b"] = 1
        
    try:
        coeff["c"] = eval(tokens[2])
    except:
        coeff["c"] = 0
    
    return coeff


def quad(eq): #solves
    coeff=eq_split(eq)
    for key in coeff:
        coeff[key] = int(coeff[key])
    
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
    
quad("4x**2=-5x+6")
