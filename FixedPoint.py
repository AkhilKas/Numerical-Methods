import math as m

#Relative error
epsilon = 0.00001

def function(x):
    
    #Claculate value of function at a particular point
    return m.pow(x, 2) - x - 2

def gFunction(x):
    
    #Calculate value of rearranged function (x = g(x))
    return 1 + 2/x

#Algorithm
def FixedPoint(x):
    
    #Value of xi
    xi = gFunction(x)
    
    #Continue as long as value > relative error
    while(abs(x) >= epsilon):
        xi = gFunction(x)
        x = xi
        
    #Print root accurate to 5 decimal places
    print("Root : ",end="")
    print('%0.5f'%x)

def mainFunction():
    
    #Input initial guess
    x0 = float(input("Enter initial guess : "))
    
    FixedPoint(x0)

#Call main fuction
mainFunction()