
import numpy as np

def submatrix_with_particular_sum(main_matrix):
    rows, cols = main_matrix.shape
    sub_matrices = []
    
    for sub_rows in range(1, rows + 1):
        for sub_cols in range(1, cols + 1):
            for i in range(rows - sub_rows + 1):
                for j in range(cols - sub_cols + 1):
                    sub_matrix = main_matrix[i:i+sub_rows, j:j+sub_cols]
                    if np.sum(sub_matrix) == -25:
                        sub_matrices.append(sub_matrix)
        
    return sub_matrices
