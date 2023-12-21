
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    r, c = matrix.shape
    for i in range(r):
        for j in range(c):
            for k in range(i, r):
                for l in range(j, c):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.prod(submatrix.shape) == 97:
                        count += 1
    return count
