import numpy as np
def submatrix_with_particular_sum(mat):
    return [submat for submat in np.where(np.sum(submat, axis=1) == -83)[0] if len(submat) == len(set(submat))]
