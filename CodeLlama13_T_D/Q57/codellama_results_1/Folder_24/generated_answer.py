
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    for i in range(rows-1):
        for j in range(cols-1):
            sub_matrix = matrix[i:i+2,j:j+2]
            if np.sum(sub_matrix) == -36:
                return [sub_matrix]
    return []
