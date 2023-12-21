
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    nrows, ncols = matrix.shape
    target_sum = 38
    
    for i in range(nrows):
        for j in range(ncols):
            for k in range(i, nrows):
                for l in range(j, ncols):
                    submatrix = matrix[i:k+1, j:l+1]
                    if submatrix.sum() == target_sum:
                        submatrices.append(submatrix.tolist())

    return submatrices
