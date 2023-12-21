import numpy as np
def submatrix_with_particular_sum(matrix):
    row_sum = np.sum(matrix, axis=1)
    col_sum = np.sum(matrix, axis=0)
    return np.where(row_sum == col_sum == 78, matrix, np.zeros((0, 0))).tolist()
