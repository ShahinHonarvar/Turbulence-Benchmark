import numpy as np
def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray):
        return []
    matrix = np.array(matrix)
    return np.where(np.sum(matrix, axis=1) == 3, np.where(np.sum(matrix, axis=0) == 3, np.array(range(matrix.shape[0])), np.array(range(matrix.shape[1]))))
