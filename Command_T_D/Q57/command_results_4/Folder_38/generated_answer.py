import numpy as np
def submatrix_with_particular_sum(arr):
    rows = np.arange(len(arr))
    columns = np.arange(len(arr[0]))
    return np.where(
        np.sum(arr[rows][columns], axis=1) == 34,
        np.s_[rows][columns],
        np.empty(len(rows), dtype=np.intp),
    )
