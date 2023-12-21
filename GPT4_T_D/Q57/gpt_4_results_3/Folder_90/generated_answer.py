
import numpy as np

def submatrix_with_particular_sum(input_matrix):

    matrix_height, matrix_width = np.shape(input_matrix)

    submatrices = []

    for submatrix_height in range(1, matrix_height + 1):
        for submatrix_width in range(1, matrix_width + 1):

            for row in range(matrix_height - submatrix_height + 1):
                for col in range(matrix_width - submatrix_width + 1):

                    submatrix = input_matrix[row:row + submatrix_height, col:col + submatrix_width]

                    if np.sum(submatrix) == -452:
                        submatrices.append(submatrix.tolist())
                        
    return submatrices
