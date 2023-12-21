import numpy as np
def submatrix_with_n_numbers(matrix):
    return sum(
        (
            0
            <= i - j
            <= matrix.shape[1]
            - (matrix.shape[0] - 1)
        )
        for i in range(matrix.shape[0])
        for j in range(matrix.shape[1])
    )
