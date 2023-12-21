import numpy as np
def submatrix_with_n_numbers(matrix):
    if matrix.size == 0:
        return 0
    matrix = np.array(matrix)
    count = 0
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            if matrix[row][col] == 41:
                count += 1
            else:
                break
    return count
