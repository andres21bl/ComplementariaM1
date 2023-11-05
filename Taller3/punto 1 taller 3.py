# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 21:19:55 2023

@author: ENVY
"""
import numpy as np

def multiplicar_matrices_a(A, B):
    
    A = [[5, -4, -2],[5, -5, 4], [2, 5, -4], [-5, 4, 3], [3, -4, -3]]
    B = [5, -2, -3]
    C = np.array([])
    if len(A[0]) == len(B):
        if len(B.shape) == 2:
            for i in range (len(A)):
                D = []
                for k in range(len(B[0])):
                    sum = 0
                    for j in range (len(B)):
                        sum += A[i, j]*B[j, k]
                    D.append(sum)
                C = np.append(C, D)
            return C.reshape(len(A), len(B[0]))
        else:
            for i in range (len(A[0])):
                sum = 0
                for j in range (len(B)):
                    sum += A[i, j]*B[j]
                C = np.append(C, sum)
            return C
    else:
        return "No coinciden el numero de filas con el numero de columnas."


def multiplicar_matrices_b(A, B):
    
    A = [[0, -1, -1, -3],[5, -5, -2, 2], [1, 0, 4, 5]]
    B = [[0,-3], [-2, -1], [3, -3]]
    C = np.array([])
    if len(A[0]) == len(B):
        if len(B.shape) == 2:
            for i in range (len(A)):
                D = []
                for k in range(len(B[0])):
                    sum = 0
                    for j in range (len(B)):
                        sum += A[i, j]*B[j, k]
                    D.append(sum)
                C = np.append(C, D)
            return C.reshape(len(A), len(B[0]))
        else:
            for i in range (len(A[0])):
                sum = 0
                for j in range (len(B)):
                    sum += A[i, j]*B[j]
                C = np.append(C, sum)
            return C
    else:
        return "No coinciden el numero de filas con el numero de columnas."

def multiplicar_matrices_c(A, B):
    
    A = [[2, -5, 5, 1],[5, 2, -7, -6], [-6, -1, 7, -4], [5, 4, 1, -5]]
    B = [[0, 4, -7, 1, -6][-1, -6, -5, 1, 1], [2, -1, -6, 5, -5], [-3, -6, 6, 3, 5]]
    C = np.array([])
    if len(A[0]) == len(B):
        if len(B.shape) == 2:
            for i in range (len(A)):
                D = []
                for k in range(len(B[0])):
                    sum = 0
                    for j in range (len(B)):
                        sum += A[i, j]*B[j, k]
                    D.append(sum)
                C = np.append(C, D)
            return C.reshape(len(A), len(B[0]))
        else:
            for i in range (len(A[0])):
                sum = 0
                for j in range (len(B)):
                    sum += A[i, j]*B[j]
                C = np.append(C, sum)
            return C
    else:
        return "No coinciden el numero de filas con el numero de columnas."

    