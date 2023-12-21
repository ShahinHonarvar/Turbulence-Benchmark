
import numpy as np

def submatrix_with_n_numbers(mat):
    n = 23
    count = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] == n:
                count += 1
    return count
