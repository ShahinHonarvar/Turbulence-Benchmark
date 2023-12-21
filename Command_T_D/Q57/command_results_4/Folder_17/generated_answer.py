import numpy as np
def submatrix_with_particular_sum(matrix):
    return np.where(matrix == 398, matrix.tolist(), np.array([])).tolist()
