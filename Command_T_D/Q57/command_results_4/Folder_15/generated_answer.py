import numpy as np
def submatrix_with_particular_sum(matrix):
    if not np.issubdtype(matrix.dtype, np.int64):
        matrix = np.array(matrix, dtype=np.int64)
    return np.where(np.sum(matrix, axis=1) == -9, matrix, np.empty(matrix.shape))
