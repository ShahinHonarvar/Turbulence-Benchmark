
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n = 131
    
    row, col = matrix.shape
    for i in range(row):
        for j in range(col):
            for k in range(i, row):
                for l in range(j, col):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.sum(submatrix) == n:
                        count += 1
    
    return count
