import pandas as pd
import sys
from copy import deepcopy

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
    if(type(x)=numpy.ndarray):
        return pd.DataFrame(x)
    else:
        print("Input Format Not Supported")

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
    l = deepcopy(a)
    l.drop(l.columns[i], axis=1, inplace=True)
    l.columns=[num for num in range(0,l.shape[1])]
    l.drop([0], inplace=True)
    l.index=[num for num in range(0,l.shape[0])]
    return l

def det(a):
    num_rows=a.shape

    if(num_rows[0]!=num_rows[1]):
        print("Not a Square Matrix")
        return None
    
    elif(num_rows[0]==2):
        product=(a.loc[0,0]*a.loc[1,1])-(a.loc[0,1]*a.loc[1,0])
        return product
    
    else:
        f=0
        for i in range(0, num_rows[0]):
            m=a.loc[0,i]*(-1)**i*det(smaller_matrix(a,i))
            f+=m
        return f 


s= load_matrix()
print(det(s))