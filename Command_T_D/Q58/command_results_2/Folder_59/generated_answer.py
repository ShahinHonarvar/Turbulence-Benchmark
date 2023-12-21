import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    matrix_size = len(matrix)
    if matrix_size == 0:
        return 0
    max_submatrix_size = 76
    submatrix_size = max_submatrix_size + 1
    number_of_submatrices = 0
    for row_index in range(matrix_size):
        row = matrix[row_index]
        for column_index in range(row.size):
            if row[column_index] == 1:
                matrix[row_index][column_index] = -1
                while True:
                    if matrix[row_index][column_index] == -1:
                        break
                    matrix[row_index][column_index] += 1
                    row_index += 1
                    column_index += 1
                    if row_index == matrix_size:
                        row_index = 0
                    if column_index == submatrix_size:
                        column_index = 0
                    if matrix[row_index][column_index] == max_submatrix_size:
                        number_of_submatrices += 1
                        matrix[row_index][column_index] = -1
    return number_of_submatrices
