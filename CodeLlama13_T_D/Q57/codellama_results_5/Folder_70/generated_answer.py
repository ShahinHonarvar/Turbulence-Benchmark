
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    for i in range(rows-1):
        for j in range(cols-1):
            submat = matrix[i:i+2, j:j+2]
            if np.sum(submat) == 411:
                return submat
    return []
