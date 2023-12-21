import numpy as np
def submatrix_with_particular_sum(A):
    return [B for B in np.split(A, np.where(A == 2)[0], axis=1)]
