
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    sub_matrix = matrix[i:k+1, j:l+1]
                    if np.sum(sub_matrix) == -20:
                        result.append(sub_matrix.tolist())
    return result
