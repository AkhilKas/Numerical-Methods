epsilon = 0.00001

def mainfun():
    
    a = float(input("Enter lower bound of interval : "))
    b = float(input("Enter upper bound of interval : "))
    bisection(a, b)
    
def function(x):
    
    #Find value of function at a particular point
    return x*x - 3

def bisection(x, y):
    
    #Check if assumed interval contains the root
    if function(x)*function(y) > 0:
        print("The assumed interval is incorrect")
    
    c = x
    
    while((y - x) >= epsilon):
        
        #Find mid-point
        c = (x + y)/2
        
        #Check if mid-point is root
        if function(c) == 0:
            print("Root : "+str(c))
            
        #Decide which 2 values to use for further steps (if any)
        if function(c)*function(x) < 0:
            y = c
        else:
            x = c
            
    print("Root : ",end="")
    print('%.5f'%c)

mainfun()