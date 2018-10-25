# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 12:10:50 2018

@author: Ammar
"""


def identity(m):
    result = []
    for i in range(m):
        row = [0]*m
        row[i] = 1
        result.append(row)
    return result

def matrix_inverse(a):
    # accepts any square, non-singular matrix of dimension 2x2 or bigger
    #LU decomposition
    L = identity(len(a))
    for j in range(0, len(a[0])):
        for i in range(j + 1, len(a)):
            if a[i][j] != 0:
                mc = a[i][j] / a[j][j]
                eliminator = [a[j][x] * mc for x in range(len(a[j]))]
                trouble_row = [a[i][y] - eliminator[y] for y in range(len(a[i]))]
                a[i] = trouble_row
                L[i][j] = mc

    U = a

    #forward-substitution
    idm = identity(len(a))
    Z = [[0 for y in range(len(U))] for x in range(len(L))]
    for f in range(len(L[0])):
        for r in range(len(L)):
            Z[r][f] += idm[r][f] - sum([L[r][x] * Z[x][f] for x in range(len(L[0]))])

    #back-substitution
    X = [[0 for y in range(len(U))] for x in range(len(L))]
    for e in range(len(X[0])):
        for w in range(-1, -(1 + len(U)), -1):
            for q in range(-1, -(1 + len(U[0])), -1):
                if U[w][q] == U[w][w]:
                    X[w][e] += Z[w][e] / U[w][q]
                else:
                    Z[w][e] -= U[w][q] * X[q][e]

    return X