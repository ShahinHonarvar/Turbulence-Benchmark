import numpy as np
def submatrix_with_particular_sum(arr):
    if arr.shape[0] < 2 or arr.shape[1] < 2:
        return []
    matrix_size = arr.shape[0] * arr.shape[1]
    row_sums = np.sum(arr, axis=0)
    col_sums = np.sum(arr, axis=1)
    return np.where(
        (row_sums == -47) & (col_sums == -47),
        arr,
        None
    )
