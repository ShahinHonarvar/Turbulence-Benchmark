
import numpy as np

def submatrix_with_n_numbers(mat):
    n = 191
    count = 0
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            curr = mat[i][j]
            if curr == n:
                count += 1
    return count
