# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 17:05:22 2023

@author: ENVY
"""

import numpy as np
import matplotlib.pyplot as plt


n = 5
probabilidades = np.linspace(0, 1, 100)
N = 100
resultados = []
for p in probabilidades:
    
    aceptados = 0
    lista = np.random.binomial(n, p, size=10000)
    
    for i in range(len(lista)):
            if lista[i] <= 1:
                aceptados += 1
    
    probabilidad = aceptados / N
    resultados.append(probabilidad)
    
n = 25
probabilidades = np.linspace(0, 1, 100)
N = 100
resultados2 = []
for p in probabilidades:
    
    aceptados = 0
    lista = np.random.binomial(n, p, size=10000)
    
    for i in range(len(lista)):
            if lista[i] <= 5:
                aceptados += 1
    
    probabilidad2 = aceptados / N
    resultados2.append(probabilidad2)
    
plt.plot(probabilidades, resultados, label="n=5")
plt.plot(probabilidades, resultados2, label="n=25") 

print(str("Para un rango de p entre 0 y 0.10, es mejor usar el segundo modelo, donde n=25 y a = 5, ya que la probabilidad de aceptación es mas alta. Para un valor de p superior a 0.3, es mejor usar el primer modelo, donde n=5 y a=1."))




    

    
                




    
