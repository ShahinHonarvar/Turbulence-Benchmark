
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    if np.sum(matrix[i:k+1, j:l+1]) == -10:
                        submatrices.append(matrix[i:k+1, j:l+1].tolist())
    
    return submatrices
