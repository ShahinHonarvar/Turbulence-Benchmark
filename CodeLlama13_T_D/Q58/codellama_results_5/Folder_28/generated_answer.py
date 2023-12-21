
import numpy as np
def submatrix_with_n_numbers(mat):
    n = len(mat)
    m = len(mat[0])
    count = 0
    
    for i in range(n - 2):
        for j in range(m - 2):
            if mat[i][j] == 37 and \
               mat[i + 1][j] == 37 and \
               mat[i][j + 1] == 37 and \
               mat[i + 1][j + 1] == 37:
                count += 1
    
    return count
