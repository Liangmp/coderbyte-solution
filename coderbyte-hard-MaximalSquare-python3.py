#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:54:05 2019

@author: taylorliang
"""
def MaximalSquare(strArr):
    l = list([[int(x) for x in s] for s in strArr])
    #print(l)
    
    row = len(strArr)
    col = len(strArr[0])
    F = min(row, col)
    #print("row, col = ", row, ', ', col)
    #print("original F =", F)
    
    for f in range(F, 0, -1):  # descending searching
        #print("======================================================\nfilter size = ", f)
        for i in range(0, row-f+1):    # from row to row (filter goes from upper to bottom)   
            # if f == row, do this for loop only once
            # i is the row index of the matrix
            for j in range(0, col-f+1): # from column to column (filter goes from left to right)
                # if f == col, do this loop only once
                # j is the column index of the matrix
                # strArr[i][j] is the upper left corner of the submatrix
                #print(f'Top left coordinate of the submatrix is: i, j = {i}, {j}')
                multiply = 1
                
                # l[m][n] is the elements of the submatrix
                for m in range(i, f+i):
                    for n in range(j, f+j):
                        #print(f'm, n = {m}, {n}')
                        multiply *= l[m][n]
                        #print(f'multiply = {multiply}')
                ## after all the multiply operator:
                if multiply == 1:
                    return f*f
    return 0
    
# copy and paste the test case here:
strArr = ["0111", "1111", "1111", "1111"]
print(MaximalSquare(strArr))