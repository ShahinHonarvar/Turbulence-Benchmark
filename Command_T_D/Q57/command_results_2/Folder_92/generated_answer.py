import numpy as np
def submatrix_with_particular_sum(matrix):
    return [row[:] for row in np.where(np.sum(matrix, axis=1) == -3)[0] if row.shape[0] > 1]
