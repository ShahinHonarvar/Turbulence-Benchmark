import numpy as np
def submatrix_with_particular_sum(matrix):
    return [np.array(r) for r in np.where(matrix == -50)]
