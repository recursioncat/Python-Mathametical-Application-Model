import pandas as pd
import sys
from copy import deepcopy
import numpy as np

# Load Matrix

def load_matrix(x=None):                                                      #IF function Passed Without Any Argument
    if(x==None):
        matrix = sys.stdin.read()                                             #Reads Until Ctrl+z and enter Pressed Twice
        matrix = matrix.strip().split('\n')                                   #Breaks the list into rows whenever there is a linebreak
        matrix = [x if '\x1a' not in x else x[:len(x)-1] for x in matrix]     #weird bugfix: ctrl +z also appears, deletes that
        matrix = [x.split(' ') for x in matrix]                                
        matrix = [[int(l) for l in row] for row in matrix]                    #converts each value into an int                
        print("\nData Loaded Successfully")
        return pd.DataFrame(matrix)
    
    if(type(x)==list):                                                        #if Function passed as a list
        matrix = x
        return pd.DataFrame(matrix)
    
    if(type(x)==numpy.ndarray):
        return pd.DataFrame(x)
    
    else:
        print("Input Format Not Supported")
        return None

#Find Sum Of Matrix

def mat_sum(a, b):
    result = a.add(b)
    return result

#Find the Difference

def mat_diff(a, b):
    result=a.sub(b)
    return result

#Determinant

def smaller_matrix(a,i):
    l = deepcopy(a)                                                  #Copy The Matrix
    l.drop(l.columns[i], axis=1, inplace=True)
    l.columns=[num for num in range(0,l.shape[1])]                   #Drop And Rename The Columns and Rows
    l.drop([0], inplace=True)
    l.index=[num for num in range(0,l.shape[0])]
    return l

def det(a):
    num_rows=a.shape

    if(num_rows[0]!=num_rows[1]):
        print("Not a Square Matrix")
        return None
    
    elif(num_rows[0]==2):
        product=(a.loc[0,0]*a.loc[1,1])-(a.loc[0,1]*a.loc[1,0])       #Determinant Of a 2x2 Square Matrix
        return product
    
    else:
        f=0
        for i in range(0, num_rows[0]):
            m=a.loc[0,i]*(-1)**i*det(smaller_matrix(a,i))             #Pos * (-1)^ position * determinant of smaller Matrix
            f+=m
        return f 


# Multiplication
def mul(mat1,mat2):
    if(mat1.shape[0] != mat2.shape[1]):
        print("Multiplication Of Matrices Not Possible")
        return None
    else:
        prod = pd.DataFrame(index=range(mat1.shape[0]), columns=range(mat2.shape[1]))   #Create An Empty Dataframe
        for i in range(prod.shape[0]):
            for j in range(prod.shape[1]):
                right = mat1.iloc[i, :].values                                          #List of Rows of the First Matrix
                down = mat2.iloc[:, j].values                                           #List of Columns of The Second Matrix (Waterfall Method)
                res = np.dot(right, down)
                prod.iloc[i, j] = res
        return prod