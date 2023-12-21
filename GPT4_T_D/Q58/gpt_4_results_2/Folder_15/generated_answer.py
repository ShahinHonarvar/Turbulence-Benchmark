
import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for i in range(m):
        for j in range(n):
            for p in range(i, m):
                for q in range(j, n):
                    submatrix = matrix[i:p+1, j:q+1]
                    if submatrix.size == 2:
                        count += 1
    return count
