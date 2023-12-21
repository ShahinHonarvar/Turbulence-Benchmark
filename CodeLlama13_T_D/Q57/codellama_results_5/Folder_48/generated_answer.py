
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i+1, rows):
                for l in range(j+1, cols):
                    submat = matrix[i:k+1, j:l+1]
                    if np.sum(submat) == -261:
                        return [submat]
    return []
