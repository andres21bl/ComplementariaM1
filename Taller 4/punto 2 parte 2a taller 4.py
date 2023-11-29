# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 15:39:06 2023

@author: ENVY
"""
import numpy as np

def parte_a():
    p = 1
    N = 100000
    resultados = np.random.poisson(1, N)
    n = 0
    
    while p > 0.01:
        
        probabilidad = 0
        
        
        for i in range(len(resultados)):
            
            if resultados[i] >= n:
                probabilidad += 1
        
        p = (probabilidad/N)
        n += 1
        
    return p, n
    

print(parte_a())


