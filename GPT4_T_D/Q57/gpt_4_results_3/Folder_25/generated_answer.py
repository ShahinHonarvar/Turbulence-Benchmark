
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    sub_matrices = []
    
    for sub_matrix_height in range(1, rows + 1):
        for sub_matrix_width in range(1, cols + 1):

            for r in range(rows - sub_matrix_height + 1):
                for c in range(cols - sub_matrix_width + 1):

                    sub_matrix = matrix[r:r+sub_matrix_height, c:c+sub_matrix_width]
                    if np.sum(sub_matrix) == -20:
                        sub_matrices.append(sub_matrix)
    
    return sub_matrices
