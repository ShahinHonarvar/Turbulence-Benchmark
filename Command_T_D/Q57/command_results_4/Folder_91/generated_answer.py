import numpy as np
def submatrix_with_particular_sum(matrix):
    if np.sum(matrix) != -6:
        return []
    row_idx = np.where(np.sum(matrix, axis=1) == -6)[0]
    col_idx = np.where(np.sum(matrix, axis=0) == -6)[0]
    return [[row[col] for col in range(len(row))] for row in matrix[row_idx][col_idx]]
