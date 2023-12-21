import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(
        np.logical_or(
            np.all(np.hstack((arr[0] == i, arr[1] == i, arr[2] == i)),
            np.all(np.vstack((arr[0] == j, arr[1] == j, arr[2] == j)),
        )
        for i in range(len(arr[0]))
        for j in range(len(arr[1])),
    )
