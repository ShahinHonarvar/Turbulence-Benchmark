import numpy as np
def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    return [
        [
            [
                matrix[row][col]
                for col in range(row, matrix.shape[1], -1)
            ]
            for row in range(matrix.shape[0])
        ]
        for matrix in range(-64, matrix.shape[0] + 64)
    ]
