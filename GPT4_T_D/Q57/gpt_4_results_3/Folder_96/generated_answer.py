
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    dims = matrix.shape
    for sub_matrix_height in range(1, dims[0] + 1):
        for sub_matrix_width in range(1, dims[1] + 1):
            for i in range(dims[0] + 1 - sub_matrix_height):
                for j in range(dims[1] + 1 - sub_matrix_width):
                    sub_matrix = matrix[i:i+sub_matrix_height, j:j+sub_matrix_width]
                    if np.sum(sub_matrix) == -63:
                        result.append(sub_matrix)
    return result
