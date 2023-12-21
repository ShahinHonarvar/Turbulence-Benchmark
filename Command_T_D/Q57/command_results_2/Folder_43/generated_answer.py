import numpy as np
def submatrix_with_particular_sum(matrix):
    return [
        (
            np.arange(
                matrix[i][j],
                matrix[i][j+1] + 1
            )
            + np.arange(
                matrix[i+1][j],
                matrix[i+1][j+1] + 1
            )
            + np.arange(
                matrix[i+2][j],
                matrix[i+2][j+1] + 1
            )
        )
        for i in range(len(matrix)-3)
        for j in range(len(matrix)-3)
    ]
