
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape
    for i in range(m):
        for j in range(n):
            for x in range(i, m):
                for y in range(j, n):
                    submatrix = matrix[i:x+1, j:y+1]
                    if np.isin(111, submatrix):
                        count += 1
    return count
