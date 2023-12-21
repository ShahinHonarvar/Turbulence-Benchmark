
import numpy as np

def submatrix_with_particular_sum(matrix):
    res = []
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for i in range(row + 1, matrix.shape[0] + 1):
                for j in range(col + 1, matrix.shape[1] + 1):
                    submatrix = matrix[row:i, col:j]
                    if np.sum(submatrix) == -57:
                        res.append(submatrix.tolist())
    return res
