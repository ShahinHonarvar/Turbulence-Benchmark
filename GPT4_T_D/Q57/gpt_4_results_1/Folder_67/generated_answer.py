
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    submatrices_that_sum_to_40 = []
    
    for sub_matrix_height in range(1, rows + 1):
        for sub_matrix_width in range(1, cols + 1):
            for row in range(rows - sub_matrix_height + 1):
                for col in range(cols - sub_matrix_width + 1):
                    sub_matrix = matrix[row : row + sub_matrix_height, col : col + sub_matrix_width]
                    if np.sum(sub_matrix) == 40:
                        submatrices_that_sum_to_40.append(sub_matrix.tolist())
    
    return submatrices_that_sum_to_40
