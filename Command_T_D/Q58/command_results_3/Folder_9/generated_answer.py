import numpy as np
def submatrix_with_n_numbers(matrix):
    return np.sum(
        np.where(
            np.where(
                matrix == 33,
                1,
                0
            )
            == 1
        )
        == 3
    )
