
import numpy as np

def submatrix_with_n_numbers(matrix):
    count_of_submatrices = 0
    rows = matrix.shape[0]
    cols = matrix.shape[1]
    
    for submatrix_rows in range(1, rows+1):
        for submatrix_cols in range(1, cols+1):
            if submatrix_rows * submatrix_cols == 28:
                count_of_submatrices += (rows - submatrix_rows + 1) * (cols - submatrix_cols + 1)
                
    return count_of_submatrices
