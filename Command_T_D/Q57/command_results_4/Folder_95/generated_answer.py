import numpy as np
def submatrix_with_particular_sum(arr):
    mat = np.array(arr)
    col_sums = np.sum(mat, axis=0)
    row_sums = np.sum(mat, axis=1)
    row_idxs = np.where(row_sums == 19)[0]
    col_idxs = np.where(col_sums == 19)[0]
    return [[x[i] for x in mat[row_idxs, col_idxs]] for i in range(len(row_idxs)) if row_idxs[i]]
