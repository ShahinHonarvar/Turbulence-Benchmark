import numpy as np
def submatrix_with_particular_sum(A):
    A = np.array(A)
    return np.where(A == -44).T[0].tolist()
