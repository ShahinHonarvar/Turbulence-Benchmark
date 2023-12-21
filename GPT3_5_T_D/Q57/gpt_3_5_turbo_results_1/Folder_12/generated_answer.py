
import numpy as np

def submatrix_with_particular_sum(matrix):
    target_sum = -83
    submatrices = []
    
    rows, cols = matrix.shape
    
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k+1, j:l+1]
                    if submatrix.sum() == target_sum:
                        submatrices.append(submatrix.tolist())
    
    return submatrices
