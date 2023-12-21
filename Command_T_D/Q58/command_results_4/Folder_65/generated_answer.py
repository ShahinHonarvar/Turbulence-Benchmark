import numpy as np
def submatrix_with_n_numbers(arr):
    return sum(
        (
            1
            for i in range(arr.shape[0])
            for j in range(i, arr.shape[1])
            if np.all(arr[i:j]) == 35
        )
    )
