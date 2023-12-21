
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    m, n = matrix.shape

    for i in range(m):
        for j in range(n):
            for p in range(i, m):
                for q in range(j, n):
                    submatrix = matrix[i:p+1, j:q+1]
                    if np.sum(submatrix) == 43:
                        count += 1

    return count
