
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []

    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for submatrix_size_row in range(1, matrix.shape[0] + 1 - row):
                for submatrix_size_col in range(1, matrix.shape[1] + 1 - col):
                    submatrix = matrix[row:row + submatrix_size_row, col:col + submatrix_size_col]
                    if np.sum(submatrix) == -87:
                        result.append(submatrix.tolist())

    return result
