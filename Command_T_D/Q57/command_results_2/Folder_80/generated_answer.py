import numpy as np
def submatrix_with_particular_sum(arr):
    matrix = np.array(arr)
    row_sums = np.sum(matrix, axis=1)
    column_sums = np.sum(matrix, axis=0)
    if not (row_sums == 245).any():
        return []
    row_inds = np.where(row_sums == 245)[0]
    column_inds = np.where(column_sums == 245)[0]
    submat_inds = np.where(row_sums == 245 & column_sums == 245)[0]
    return [matrix[submat_inds].tolist()]
