# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 18:38:44 2023

@author: ENVY
"""

import numpy as np

def punto_c():
    
    N = 100000
    matriz1 = np.random.poisson(1, N)
    matriz2 = np.random.poisson(1, N)
    matriz3 = np.random.poisson(1, N)
    c = 0
    
    for i in range (len(matriz1)):
        if matriz1[i]== 1 and matriz2[i] != 1 and matriz3[i] != 1:
            c += 1
        if matriz1[i]!= 1 and matriz2[i] == 1 and matriz3[i] != 1:
            c += 1
        if matriz1[i]!= 1 and matriz2[i] != 1 and matriz3[i] == 1:
            c += 1
    p = c/N
    return p

def punto_d():
    
    c = 0
    N = 100000
    matriz1 = np.random.poisson(1, N)
    matriz2 = np.random.poisson(1, N)
    matriz3 = np.random.poisson(1, N)
    
    
    for i in range (len(matriz1)):
        if matriz1[i] + matriz2[i] + matriz3[i] ==3:
            c += 1
    
    prob = c/N
    
    return prob

print(str("En un periodo de 4 horas se espera una desconexión, por ende en 3 periodos de 4 horas consecutivos se esperan 3 desconecciones. La probabilidad de 3 desconecciones en 3 periodos consecutivos de 4 horas es de"))     
print(punto_d())
          
    
    
             
    
    
