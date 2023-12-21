import numpy as np
def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    return np.where(matrix.sum(axis=1) == 78)[0].tolist()
