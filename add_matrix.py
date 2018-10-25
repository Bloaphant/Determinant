# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 12:08:46 2018

@author: Ammar
"""

def matrix_add(a, b):
    result_list = []

    for i in range(len(a)):
        listA = a[i]
        listB = b[i]
        newlist = []
        for t in range(len(listA)):
            newlistres = listA[t] + listB[t]
            newlist.append(newlistres)

        result_list.append(newlist)

    return result_list
