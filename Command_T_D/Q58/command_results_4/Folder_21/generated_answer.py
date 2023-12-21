import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    matrix_size = len(matrix)
    matrix_width = len(matrix[0])
    submatrix_size = matrix_size * (matrix_size - 1) // 2
    matrix_set = set(matrix)
    return sum(sum(1 for i in range(matrix_width) if matrix[row][i] in matrix_set) == 139 for row in range(matrix_size))
