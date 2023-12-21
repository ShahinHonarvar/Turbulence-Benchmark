import numpy as np
def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    if matrix.shape[0] < matrix.shape[1]:
        matrix = np.rot90(matrix)
    if matrix.shape[0] == matrix.shape[1]:
        matrix = np.pad(matrix, ((0, 0), (0, 8 - matrix[0][-1]), (0, 0)))
    return [(row, row + 8) for row in range(matrix.shape[0]) if matrix[row][:8] == 8]
