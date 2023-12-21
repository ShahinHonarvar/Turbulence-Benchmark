
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i+1, rows+1):
                for l in range(j+1, cols+1):
                    sub_matrix = matrix[i:k, j:l]
                    if np.sum(sub_matrix) == 997:
                        result.append(sub_matrix.tolist())
    return result
