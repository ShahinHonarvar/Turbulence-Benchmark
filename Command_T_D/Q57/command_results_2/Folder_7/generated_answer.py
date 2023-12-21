import numpy as np
def submatrix_with_particular_sum(mat):
    return [row for row in np.where(np.sum(row, axis=1) == -128)[0] if len(row) > 1]
