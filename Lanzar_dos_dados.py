# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 21:50:15 2020

@author: uribe
"""

'''Al lanzar 2 dados 100 veces, cual es resultado mas probable'''
import numpy as np
import matplotlib.pyplot as plt

import random as rd
dado1=np.zeros(7)
dado2=np.zeros(7)
resultados=np.zeros(101)
for i in range(1,101):
    r1=rd.randint(1,6)
    r2=rd.randint(1,6)
    resultados[i]=r1+r2
print(resultados[1:101])
plt.plot(resultados[1:101])
