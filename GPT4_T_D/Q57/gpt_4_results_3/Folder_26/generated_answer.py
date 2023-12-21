
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    sub_matrices = []
    
    for sub_matrix_row in range(1, rows + 1):
        for sub_matrix_col in range(1, cols + 1):
            for row in range(0, rows - sub_matrix_row + 1):
                for col in range(0, cols - sub_matrix_col + 1):
                    sub_matrix = matrix[row: row + sub_matrix_row, col: col + sub_matrix_col]
                    if np.sum(sub_matrix) == 997:
                        sub_matrices.append(sub_matrix)
                        
    return sub_matrices
