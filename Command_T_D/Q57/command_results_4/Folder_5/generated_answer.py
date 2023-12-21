import numpy as np
def submatrix_with_particular_sum(mat):
    return [
        np.array(row) for row in np.where(np.sum(row, axis=1) == -43)
    ]
