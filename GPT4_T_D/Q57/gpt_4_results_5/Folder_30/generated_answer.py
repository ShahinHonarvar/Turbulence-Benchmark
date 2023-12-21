
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices_21 = []

    for i in range(rows):
        for j in range(cols):
            for p in range(i, rows):
                for q in range(j, cols):
                    submatrix = matrix[i:p+1, j:q+1]
                    if submatrix.sum() == 21:
                        submatrices_21.append(submatrix)
                        
    return submatrices_21
