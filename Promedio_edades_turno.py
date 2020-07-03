# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 15:21:39 2020

@author: uribe
"""
'''Para un numero no determinado de trabajadores, indicar la edad promedio por turno.
Sabiendo que se registran las edades y los turnos (M, T y N) para cada trabajador.'''
############################Bucle for
#Turno manana
m=int(input("Ingrese numero de trabajadores turno M: "))
suma=0
for i in range(1,m+1):
    edad=float(input("Ingrese edades del turno [" +str(i)+"]: "))
    suma+=edad
Promedio_m=suma/m
print(Promedio_m)

#Turno tarde
t=int(input("Ingrese numero de trabajadores turno T: "))
suma=0
for i in range(1,t+1):
    edad=float(input("Ingrese edades del turno [" +str(i)+"]: "))
    suma+=edad
Promedio_t=suma/t
print(Promedio_t)

#Turno noche
n=int(input("Ingrese numero de trabajadores turno N: "))
suma=0
for i in range(1,n+1):
    edad=float(input("Ingrese edades del turno [" +str(i)+"]: "))
    suma+=edad
Promedio_n=suma/n
print(Promedio_n)
    
#####################################Mediante Matrices
import numpy as np
m=int(input("Ingrese numero de trabajadores turno M: "))
t=int(input("Ingrese numero de trabajadores turno T: "))
n=int(input("Ingrese numero de trabajadores turno N: "))
max_num=max(m,t,n)
s=(3,max_num+1)
Edades=np.zeros(s)
suma=[0,0,0]
Promedio=[0,0,0]

for i in range(1,m+1):
    Edades[0][i]=float(input("Ingrese edades del turno M [" +str(i)+"]: "))
    suma[0]+=Edades[0][i]
Promedio[0]=suma[0]/m

for i in range(1,t+1):
    Edades[1][i]=float(input("Ingrese edades del turno T [" +str(i)+"]: "))
    suma[1]+=Edades[1][i]
Promedio[1]=suma[1]/t

for i in range(1,n+1):
    Edades[2][i]=float(input("Ingrese edades del turno N [" +str(i)+"]: "))
    suma[2]+=Edades[2][i]
Promedio[2]=suma[2]/n

print(Promedio)
    

    
