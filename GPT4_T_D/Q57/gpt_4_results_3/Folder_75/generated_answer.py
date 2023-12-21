
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for sub_size_row in range(1, rows + 1):
        for sub_size_col in range(1, cols + 1):
            for i in range(rows - sub_size_row + 1):
                for j in range(cols - sub_size_col + 1):
                    sub = matrix[i : i + sub_size_row, j : j + sub_size_col]
                    if np.sum(sub) == 16:
                        result.append(sub)

    return result
