import numpy as np
def submatrix_with_particular_sum(mat):
    return [submat for submat in np.split(mat, np.where(np.sum(submat, axis=1) == 16)[0]) if len(submat) > 1]
