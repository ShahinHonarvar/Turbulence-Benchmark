import numpy as np
def submatrix_with_particular_sum(matrix):
    if matrix.size == 0:
        return []
    result = []
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            row_sums = np.sum(matrix[row][:col] + matrix[row][col+1:], axis=1)
            if np.sum(row_sums) == 27:
                result += [[row, col]]
    return result
