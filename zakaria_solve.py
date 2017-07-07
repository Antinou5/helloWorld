# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 15:39:16 2017

@author: Antinou5
"""


import sympy as sy
import numpy as np
import matplotlib.pyplot as plt



# plot des sol d'un polynome 

#
#a=int(input("a ?"))
#b=int(input("b ?"))
#c=int(input("c ?"))
#
#x=sy.symbols("x")
#expr= a*x**2 + b*x + c
#
#abs=np.linspace(-10,10)
#ord=np.array([])
#for i in range(len(abs)) :
#    ord=np.append(ord,expr.subs(x,abs[i]).evalf())
#    
#plt.plot(abs,ord)
#plt.show()

g1, g2, b, q= sy.symbols("g1, g2, b, q")
alpha=(sy.Rational(1,2)-sy.Rational(1,4))*sy.tan(sy.pi*sy.Rational(1,4))
eq1= sy.pi * (g1**2*b**4+g2*b**2) - alpha