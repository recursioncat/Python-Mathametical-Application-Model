import re

#We'll take multiple equations as input

#"4x+5y+7z=0, 7x+5y-11z=9, 12x+3y=19y......." ------> ["4x+5y+7z=0", 7x+5y-11z=9, ...... ]
def eq_to_list(equations):
    equation_list=re.split(",", equations)
    return equation_list

#We need to find out the variables in the equations
def find_vars(equation_list):
    nums="0123456789+-/*()= "
    list_of_variables=[]
    for equation in equation_list:
        for letters in equation:
            if letters not in nums and letters not in list_of_variables:
                list_of_variables.append(letters)
    return list_of_variables

#Modified Change Signs Function Series
def isdigit(string):
    if string[0]=="+" or string[0]=="-":
        string=string[1:]
    return string.isdigit()

def reverse(string):
    if string[0]=="-":
        return "+"+string[1:]
    elif string[0]=="+":
        return "-"+string[1:]
    else:
        return "-"+string
    
def change_signs(equation):
    left_side=""
    right_side=""
    equation=equation.replace(" ", "").replace("+", " +").replace("-"," -")
    splits=equation.split("=")
    
    #right side
    splits2=splits[1].split()
    for elements in splits2:
        if isdigit(elements)==False:
            left_side+=reverse(elements)
        else:
            right_side+=elements if elements[0]=="-" or elements[0]=="+" else "+"+elements
    
    #Left side
    splits3=splits[0].split()
    for elements in splits3:
        if isdigit(elements)==True:
            right_side+=reverse(elements)
            splits[0]=splits[0].replace(elements, "")
    
    
    final_equation=splits[0]+left_side+"="+right_side
    final_equation=final_equation.replace(" ", "")
    return final_equation
            

def value_extractor(equation_list, list_of_variables):
    matrix = {var: [] for var in list_of_variables}

    for equation in equation_list:
        equation = equation.replace("+", " +").replace("-", " -")
        terms = equation.split()
        
        for var in list_of_variables:
            coeff=0
            flag=0
            for term in terms:
                if var in term:
                    flag=1
                    coeff_str = re.split(var, term)[0]
                    if coeff_str=="+":
                        coeff_str="1"
                    elif coeff_str=="-":
                        coeff_str="-1"
                    coeff += int(coeff_str) if coeff_str else 1
            matrix[var].append(coeff)
            if flag==0:
                matrix[var].append(0)
        
    return matrix

def result_extractor(equations):
    result=[]
    for equation in equations:
        result.append(float(re.split("=", equation)[1]))
    return result

# Matrix and Determinant Part
def smaller_matrix(matrix, col):
    size=len(matrix)
    smaller = []
    for i in range(1, size):
        row = []
        for j in range(size):
            if j != col:
                row.append(matrix[i][j])
        smaller.append(row)
    return smaller

def det(a):
    lenght=len(a)
    if lenght == 2:
        product = (a[0][0] * a[1][1]) - (a[0][1] * a[1][0])  # Determinant Of a 2x2 Square Matrix
        return product
    else:
        f = 0
        for i in range(lenght):
            m = a[0][i] * (-1) ** i * det(smaller_matrix(a, i))  # Pos * (-1)^position * determinant of smaller Matrix
            f += m
        return f

# Main Solver
def form_matrices(var_values, results):
    list_var=list(var_values.keys())
    final_list=[]
    dic=var_values.values()
    transposed_matrix = [list(x) for x in zip(*dic)] #transposing a matrix
    d=det(transposed_matrix)

    if d==0:
        print("Equation not Uniquely Solvable")
        return None
        exit()

    for i, elements in enumerate(transposed_matrix):
        copy=list(dic)
        copy[i]=results
        copy=[list(x) for x in zip(*copy)] 
        temp=det(copy)
        final_list.append(temp)
    
    final_dict={}
    for i, ele in enumerate(final_list):
        final_dict[list_var[i]]=final_list[i]/d if final_list[i]/d !=0 else 0 #if part to fix the weird problem of -0.0
    return final_dict

# Main Function and Driver
def lin_eq(equations):
    if type(equations)!=list:
        equations=eq_to_list(equations)
    list_of_variables=find_vars(equations)
    prepared_equation=[]
    for equation in equations:
        prepared_equation.append(change_signs(equation))
    results=result_extractor(prepared_equation)
    var_values=value_extractor(prepared_equation, list_of_variables)
    return form_matrices(var_values, results)

if __name__=="__main__":

    print(lin_eq(["7x+x+y+5z=27", "4x+3y+5z=21", "6x+y+z+z=9"]))
    #it will return {'y': -3.0, 'x': 0, 'z': 6.0}
