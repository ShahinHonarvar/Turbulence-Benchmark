import numpy as np
def submatrix_with_particular_sum(matrix):
    return [
        np.sum(matrix[row:row + n, col:col + m], axis=0) == -394
        for row in range(matrix.shape[0])
        for col in range(matrix.shape[1])
        for n in range(1, matrix.shape[0] - row)
        for m in range(1, matrix.shape[1] - col)
    ]
