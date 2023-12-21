
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []

    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for submatrix_size in range(1, min(rows - row, cols - col) + 1):
                submatrix = matrix[row:row + submatrix_size, col:col + submatrix_size]
                if np.sum(submatrix) == -157:
                    result.append(submatrix.tolist())

    return result
