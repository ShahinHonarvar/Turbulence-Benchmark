import numpy as np
def submatrix_with_n_numbers(matrix):
    if matrix.shape[0] < 54 or matrix.shape[1] < 54:
        return 0
    matrix = np.array(matrix)
    cnt = 0
    for i in range(54):
        for j in range(54):
            cnt += matrix[i][j]
            matrix[i][j] = 0
    return cnt
