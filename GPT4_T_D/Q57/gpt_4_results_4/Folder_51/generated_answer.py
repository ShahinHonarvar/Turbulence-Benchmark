
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    results = []
    for size_row in range(1, rows + 1):
        for size_col in range(1, cols + 1):
            for row in range(0, rows - size_row + 1):
                for col in range(0, cols - size_col + 1):
                    submatrix = matrix[row:row + size_row, col:col + size_col]
                    if np.sum(submatrix) == -46:
                        results.append(submatrix)
    return results if len(results) > 0 else []
