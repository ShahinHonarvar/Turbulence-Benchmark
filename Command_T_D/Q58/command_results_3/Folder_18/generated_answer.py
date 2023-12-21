import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    if matrix.ndim != 2:
        return 0
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == 104:
                count += 1
    return count
