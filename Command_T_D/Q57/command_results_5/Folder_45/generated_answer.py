import numpy as np
def submatrix_with_particular_sum(matrix):
    m = np.array(matrix, dtype=np.int64)
    if m.size == 0:
        return []
    indices = np.where(np.sum(m, axis=1) == -77)
    if indices[0].size == 0:
        return []
    indices = np.array(indices, dtype=np.int64)
    return np.split(m, indices[1].size, axis=1)
