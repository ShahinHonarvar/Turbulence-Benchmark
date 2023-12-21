
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row, col = matrix.shape
    limit = min(row, col)

    for i in range(row):
        for j in range(col):
            for k in range(1, limit + 1):
                if i + k > row or j + k > col:
                    break
                sub_matrix = matrix[i:i+k, j:j+k]
                if np.sum(sub_matrix) == 67 * k * k:
                    count += 1

    return count
