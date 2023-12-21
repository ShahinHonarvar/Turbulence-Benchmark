
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n_rows, n_cols = len(matrix), len(matrix[0])
    
    for i in range(n_rows):
        for j in range(n_cols):
            for k in range(i+1, n_rows+1):
                for l in range(j+1, n_cols+1):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == 394:
                        submatrices.append(submatrix.tolist())
    
    return submatrices
