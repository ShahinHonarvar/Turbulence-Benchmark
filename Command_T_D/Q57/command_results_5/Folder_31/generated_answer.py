import numpy as np
def submatrix_with_particular_sum(arr):
    mat = np.array(arr)
    row_sums = np.sum(mat, axis=1)
    col_sums = np.sum(mat, axis=0)
    if len(row_sums) == 0 or len(col_sums) == 0:
        return []
    row_idxs = np.where(row_sums == -44)[0]
    col_idxs = np.where(col_sums == -44)[0]
    return [[x[row_idxs] for row_idx in range(len(row_idxs))]]
