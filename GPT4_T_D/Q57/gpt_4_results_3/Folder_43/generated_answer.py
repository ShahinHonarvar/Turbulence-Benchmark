
import numpy as np

def submatrix_with_particular_sum(matrix):
    sub_matrices = []
    rows, cols = matrix.shape
    
    for sub_matrix_size in range(1, min(rows, cols) + 1):
        for row in range(rows - sub_matrix_size + 1):
            for col in range(cols - sub_matrix_size + 1):
                sub_matrix = matrix[row:row+sub_matrix_size, col:col+sub_matrix_size]
                if np.sum(sub_matrix) == -81:
                    sub_matrices.append(sub_matrix)
                    
    return sub_matrices
