import numpy as np
def submatrix_with_n_numbers(mat):
    n = len(mat)
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if mat[i][j] == mat[j][k] == mat[k][i] == 16:
                    count += 1
    return count
