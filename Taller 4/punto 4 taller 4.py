# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 12:41:33 2023

@author: ENVY
"""

import numpy as np

def punto4():
    pi = np.array([0.25, 0, 0.5, 0.25])
    
    T = np.array([[0.4, 0.2, 0.2, 0.2],
                  [0.25, 0.25, 0.25, 0.25],
                  [0.3, 0.3, 0.1, 0.3],
                  [0.1, 0.1, 0.1, 0.7]])
    
    gen_g = pi[3]*T[2,3]*T[1,2]*T[3, 1]*T[1, 3]*T[0, 1]*T[0, 0]*T[0, 0] 
    
    E = np.array([[0.8, 0, 0, 0.2],
                  [0.05, 0.9, 0.1, 0.1],
                  [0.05, 0.1, 0.9, 0],
                  [0.1,0,0,0.7]])
    
    probabilidad_gen_traducido = E[3,3]*E[2, 2]*E[1, 1]*E[3,3]*E[1, 1]*E[0,0]*E[0,0]*E[0,0]
    
    return gen_g, probabilidad_gen_traducido

print(punto4())
    
    

