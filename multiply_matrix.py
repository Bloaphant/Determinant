# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 12:09:37 2018

@author: Ammar
"""


def matrix_multiplication(c, d):

    result = [[0 for y in range(len(d[0]))] for x in range(len(c))]
    for i in range(len(c)):
        for j in range(len(d[0])):
            for k in range(len(d)):
                result[i][j] += c[i][k] * d[k][j]

    return result