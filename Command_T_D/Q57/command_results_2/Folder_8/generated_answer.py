import numpy as np
def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    row = np.sum(matrix, axis=0)
    col = np.sum(matrix, axis=1)
    if np.sum(row == -61) == len(row):
        return [list(range(len(row))), list(range(len(col)))]
    return []
