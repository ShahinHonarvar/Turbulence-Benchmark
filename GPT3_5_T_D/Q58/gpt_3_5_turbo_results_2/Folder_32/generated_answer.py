
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 103
    rows, cols = matrix.shape

    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.count_nonzero(submatrix) == n:
                        count += 1
    
    return count
