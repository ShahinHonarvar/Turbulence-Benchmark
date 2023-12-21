import numpy as np
def submatrix_with_particular_sum(matrix):
    if not isinstance(matrix, np.ndarray):
        raise ValueError("input must be a numpy matrix")
    if matrix.shape[0] < matrix.shape[1]:
        matrix = np.rot90(matrix)
    return np.where(np.sum(matrix, axis=1) == 64)[0]
