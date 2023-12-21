import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(
        np.array([
            np.all(np.all(np.sum(matrix[row:row+n], axis=0) == n) for row in range(0, len(matrix)-n+1)
        ]),
        dtype=np.int64,
    ))
