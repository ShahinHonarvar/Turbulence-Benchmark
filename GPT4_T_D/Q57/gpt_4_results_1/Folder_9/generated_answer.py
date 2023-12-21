
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    row_length, col_length = matrix.shape[0], matrix.shape[1]
    for row in range(row_length):
        for col in range(col_length):
            for size in range(1, min(row_length - row, col_length - col) + 1):
                submatrix = matrix[row:row + size, col:col + size]
                if np.sum(submatrix) == -86:
                    result.append(submatrix.tolist())
    return result
