import numpy as np
def submatrix_with_particular_sum(matrix):
    return [
        np.array(submatrix, dtype=np.int32).tolist()
        for row in range(matrix.shape[0])
        for col in range(row + 1, matrix.shape[1])
        for submatrix in [[matrix[row][:col] for row in range(matrix.shape[0])]]
    ]
