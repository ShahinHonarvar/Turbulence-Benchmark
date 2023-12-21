import numpy as np
def submatrix_with_particular_sum(A):
    B = np.array(A)
    return np.where(np.sum(B,axis=2)==92)[0].tolist()
