
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(i+1, rows+1):
                for l in range(j+1, cols+1):
                    sub = matrix[i:k, j:l]
                    if np.sum(sub) == 77:
                        result.append(sub.tolist())
    return result
