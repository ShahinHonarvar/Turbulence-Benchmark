
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    sub = matrix[i:k+1, j:l+1]
                    if np.sum(sub) == -308:
                        submatrices.append(sub.tolist())
    
    return submatrices
