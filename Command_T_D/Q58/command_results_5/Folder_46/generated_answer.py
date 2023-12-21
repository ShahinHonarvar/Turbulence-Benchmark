import numpy as np
def submatrix_with_n_numbers(arr):
    return np.sum(
        np.all(
            np.all(arr[i:i+10] == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] * 10, axis=1)
            for i in range(0, len(arr), 10)
        ),
        axis=0,
    )
