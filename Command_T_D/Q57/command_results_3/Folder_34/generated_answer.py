import numpy as np
def submatrix_with_particular_sum(mat):
    return [np.matrix(row).tolist() for row in mat.tolist() if sum(row) == -13]
