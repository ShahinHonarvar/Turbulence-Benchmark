
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    n_rows, n_cols = matrix.shape
    
    for i in range(n_rows):
        for j in range(n_cols):
            for k in range(i, n_rows):
                for l in range(j, n_cols):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.sum(submatrix) == 997:
                        submatrices.append(submatrix.tolist())
    
    return submatrices
