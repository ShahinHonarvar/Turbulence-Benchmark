import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    n_submatrix = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            row_set = set(matrix[row])
            col_set = set(matrix[row][col])
            if len(row_set) == len(col_set) == 16:
                n_submatrix += 1
    return n_submatrix
