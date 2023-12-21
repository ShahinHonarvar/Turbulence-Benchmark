
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i+1, rows):
                for l in range(j+1, cols):
                    if np.sum(matrix[i:k,j:l]) == 15:
                        return matrix[i:k,j:l].tolist()
    return []
