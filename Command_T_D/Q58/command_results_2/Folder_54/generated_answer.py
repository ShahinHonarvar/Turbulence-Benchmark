import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    return np.sum(
        np.array(
            np.count_nonzero(
                np.hstack(
                    [matrix[i] for i in range(len(matrix))]),
                    dtype=np.int64
                ),
                dtype=np.int64
            ),
            dtype=np.int64
        ),
        dtype=np.int64
    )
