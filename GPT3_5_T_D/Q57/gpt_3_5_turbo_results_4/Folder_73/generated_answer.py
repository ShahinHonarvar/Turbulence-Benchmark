
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape[0], matrix.shape[1]
    
    for i in range(rows):
        for j in range(cols):
            for k in range(i+1, rows+1):
                for l in range(j+1, cols+1):
                    submatrix = matrix[i:k, j:l]
                    if np.sum(submatrix) == 93:
                        submatrices.append(submatrix.tolist())
    
    return submatrices
