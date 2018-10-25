# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 12:10:24 2018

@author: Ammar
"""


def matrix_determinant(a):
    # accepts any square matrix of dimension 2x2 or bigger
    # The determinant is only defined for square matrices

    # Gauss Elimination
    for j in range(0, len(a[0])):
        for i in range(j + 1, len(a)):
            if a[i][j] != 0:
                mc = a[i][j] / a[j][j]
                eliminator = [a[j][x] * mc for x in range(len(a[j]))]
                trouble_row = [a[i][y] - eliminator[y] for y in range(len(a[i]))]
                a[i] = trouble_row

    determinant = 1
    for k in range(len(a[0])):
        determinant *= a[k][k]

    return determinant