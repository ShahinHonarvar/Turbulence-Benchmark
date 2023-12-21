
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape[0], matrix.shape[1]
    results = []
    for top_row in range(rows):
        for left_col in range(cols):
            for bot_row in range(top_row + 1, rows + 1):
                for right_col in range(left_col + 1, cols + 1):
                    submatrix = matrix[top_row:bot_row, left_col:right_col]
                    if np.sum(submatrix) == 394:
                        results.append(submatrix)
    return results
