import numpy as np
def submatrix_with_n_numbers(arr):
    if len(arr) < 20:
        return 0
    matrix = np.full((20, 20), False, dtype=np.bool)
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            matrix[row][col] = True
    return np.sum(matrix.reshape(20, 20))
