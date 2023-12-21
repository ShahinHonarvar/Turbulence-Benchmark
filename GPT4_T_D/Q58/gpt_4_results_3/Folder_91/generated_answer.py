
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    
    for row_dimension in range(1, rows+1):
        for col_dimension in range(1, cols+1):
            if row_dimension * col_dimension == 5:
                count += (rows - row_dimension + 1) * (cols - col_dimension + 1)
                
    return count
