import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.matrix(matrix)
    m, n = len(matrix), len(matrix[0])
    if m == 0 or n == 0:
        return 0
    count = 0
    for i in range(0, m):
        for j in range(0, n):
            if matrix[i][j] == 35:
                count += 1
    return count
