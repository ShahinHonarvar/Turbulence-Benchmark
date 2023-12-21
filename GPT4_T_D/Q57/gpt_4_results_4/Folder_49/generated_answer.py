
import numpy as np

def submatrix_with_particular_sum(matrix):
    all_submatrices = []

    rows = len(matrix)
    cols = len(matrix[0]) if rows else 0

    for top_row in range(rows):
        for top_col in range(cols):
            for bottom_row in range(top_row, rows):
                for bottom_col in range(top_col, cols):
                    submatrix = matrix[top_row:bottom_row+1, top_col:bottom_col+1]
                    if np.sum(submatrix) == -42:
                        all_submatrices.append(submatrix)

    return all_submatrices
