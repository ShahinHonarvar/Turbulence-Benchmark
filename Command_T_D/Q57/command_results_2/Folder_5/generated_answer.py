import numpy as np
def submatrix_with_particular_sum(np_matrix):
    return np.where(np.array(np_matrix, dtype=np.int32) == -43).tolist()
