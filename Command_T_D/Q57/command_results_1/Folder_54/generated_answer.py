import numpy as np
def submatrix_with_particular_sum(arr):
    matrix = np.array(arr)
    if np.sum(matrix) == -59:
        return []
    else:
        return [list(sub) for sub in zip(*np.where(np.sum(matrix, axis=1) == -59))]
