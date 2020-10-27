import math as m

#This method is aplicable for functions that are continuous and have derivative at a point where value has to found

#Relative error
epsilon = 0.00001

def function(x):
    
    #Value of function at a particular point
    return 40*m.pow(x, 1.5) - 875*x + 35000

def derivative(x):
    
    #Value of derivate of fuction at a particular point
    return 60*m.pow(x, 0.5) - 875

def newton(y):
    
    h = function(y) / derivative(y)
    
    #Calculate as long as value greater than relative error
    while(abs(h) >= epsilon):
        
        h = function(y) / derivative(y)
        
        #Continuously reduce initial guess till root is obtained
        y -= h
        
    #Print root accurate to 5 decimal places
    print("Root : ",end="")
    print('%0.5f'%y)

def mainFunction():
    
    #Take initial input from user
    x0 = float(input("Enter initial guess : "))
    
    newton(x0)
        
mainFunction()