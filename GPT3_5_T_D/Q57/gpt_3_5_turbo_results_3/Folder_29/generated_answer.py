
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, cols = matrix.shape
    
    for i in range(rows):
        for j in range(cols):
            for m in range(i+1, rows+1):
                for n in range(j+1, cols+1):
                    submatrix = matrix[i:m, j:n]
                    if submatrix.sum() == 84:
                        submatrices.append(submatrix.tolist())
    
    return submatrices
