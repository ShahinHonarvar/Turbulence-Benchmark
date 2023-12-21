
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    if matrix[i:k+1, j:l+1].sum() == -936:
                        return list(matrix[i:k+1, j:l+1])
    return []
