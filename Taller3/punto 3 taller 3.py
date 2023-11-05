# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 21:34:18 2023

@author: ENVY
"""
import numpy as np


def MetodoPotencia(H, V, k):
    Valor_Minimo =  1000
    Matrix =  []

    W = V / np.sqrt(np.matmul(V.T, V))

    for i in range(k+1):
        V = np.matmul(H, W)
        W = V / np.sqrt(np.matmul(V.T, V))

    P1 = np.matmul(H, W)
    N = np.matmul(W.T, P1)

    frecuencia = np.sqrt(1 / np.abs(Valor_Minimo))
    m = np.linalg.inv(Matrix)

    Valor_Minimo = 1 / Valor_Minimo
    frecuencia = np.sqrt(np.abs(Valor_Minimo))

    return frecuencia, Valor_Minimo, N, m
