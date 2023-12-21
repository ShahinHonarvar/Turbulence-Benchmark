
import numpy as np

def submatrix_with_n_numbers(matrix):
    matrix_elements = matrix.shape[0] * matrix.shape[1]
    if matrix_elements < 68:
        return 0
    else:
        result = 0
        for m in range(matrix.shape[0]):
            for n in range(matrix.shape[1]):
                sub_matrix_elements = m * n
                if sub_matrix_elements == 68:
                    result += 1
        return result
