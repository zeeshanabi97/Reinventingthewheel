# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 12:14:48 2023

@author: m
"""
#%% Function Maker
def f(function:str,x:float,y:float = 1):
    return eval(function,{"x":x,"y":y})

#%% Equation Solver
def bisectionmethod (function:str, upperlimit:float,lowerlimit:float,steps:int = 1,tolerence:float=0.01):
    limit_divide = [lowerlimit + i*(upperlimit-lowerlimit)/steps for i in range(0,steps+1)]
    solutions = []
    for i in range(0,steps):
        fyi = f(function,limit_divide[i])
        fyip1 = f(function, limit_divide[i+1])
        if(fyi == 0):
           solutions.append(limit_divide[i])
           
           
           if(fyip1 == 0):
            solutions.append(limit_divide[i+1])
        if(fyi*fyip1<0):
            a = limit_divide[i]
            b = limit_divide[i+1]
            fsol = tolerence+1
            while(abs(fsol)>tolerence):
                sol = (a+b)/2
                fsol = f(function,sol)
                if (fyi*fsol<0):
                    b = sol
                else:
                    a = sol
            solutions.append(sol)
    return set(solutions)

def newtonraphson (function:str, initial_value:float,stepsize:float = 1,tolerence:float=0.01):
            while(abs(f(function,initial_value))>tolerence):
                derivative = forwarddifference(function, initial_value,stepsize)
                if derivative == 0:
                    derivative = backwarddifference(function, initial_value,stepsize)
                if derivative == 0:
                    derivative = centraldifference(function, initial_value,stepsize)
                if derivative == 0:
                    return "Derivative zero can not proceed."
                newvalue = initial_value-f(function,initial_value)/derivative
                initial_value = newvalue
            return initial_value
        
def regulafalsi (function:str, upperlimit:float,lowerlimit:float,steps:int = 1,tolerence:float=0.01):
    limit_divide = [lowerlimit + i*(upperlimit-lowerlimit)/steps for i in range(0,steps+1)]
    solutions = []
    for i in range(0,steps):
        fa = f(function,limit_divide[i])
        fb = f(function, limit_divide[i+1])
        if(fa == 0):
           solutions.append(limit_divide[i])
        if(fb == 0):
            solutions.append(limit_divide[i+1])
        if(fa*fb<0):
            a = limit_divide[i]
            b = limit_divide[i+1]
            sol = b
            fsol = tolerence+1
            while(abs(fsol)>tolerence):
                if fa == fb:
                    print("The method fails due to division by zero.")
                    break
                sol = (fb*a-fa*b)/(fb-fa)
                fsol = f(function,sol)
                if (fa*fsol<0):
                    b = sol
                elif(fb*fsol<0):
                    a = sol
            solutions.append(sol)
    return set(solutions)


#%% Derivative Finder
def forwarddifference(function:str,solveat:float,stepsize:float=1):
    return (f(function,solveat+stepsize)-f(function,solveat))/stepsize

def backwarddifference(function:str,solveat:float,stepsize:float=1):
    return (f(function,solveat)-f(function,solveat-stepsize))/stepsize

def centraldifference(function:str,solveat:float,stepsize:float=1):
    return (f(function,solveat+stepsize)-f(function,solveat-stepsize))/(2*stepsize)

#%% Differential Equation Solver

def eulermethod(function:str,lowerlimit:float,upperlimit:float,steps:int,initialvalue:float = 0):
    solution = [initialvalue]
    limit_divide = [lowerlimit + i*(upperlimit-lowerlimit)/steps for i in range(steps+1)]
    stepsize = limit_divide[1]-limit_divide[0]
    i = 0
    for i in range(1, steps + 1):
        x = lowerlimit + i * (upperlimit - lowerlimit) / steps
        solution.append(solution[i - 1] + f(function, x, solution[i - 1]) * stepsize)
    return(solution)
#%% Interpolation
def linearinterpolation(x:float,ys:float,xs:float):
    return (ys[0]+((x-xs[0])*(ys[1]-ys[0]))/(xs[1]-xs[0]))

regulafalsi("x**2-1.1",2,0,1,0.001)