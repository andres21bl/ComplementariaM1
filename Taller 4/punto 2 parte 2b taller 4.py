# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 17:02:40 2023

@author: ENVY
"""
import numpy as np

def parte_b():
    n = 0
    p = 1
    N = 100000
    while p > 0.02:
        
        
        cuenta = 0
        resultados = np.random.poisson(n, N)
        
        for i in range(len(resultados)):
                if resultados[i] == 0:
                    cuenta += 1
                p = cuenta/N
        n += 1        
    return p, n

print(parte_b())





