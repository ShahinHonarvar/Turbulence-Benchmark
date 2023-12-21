
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    
    rows, cols = matrix.shape
    
    for row_dim in range(1, rows + 1):
        for col_dim in range(1, cols + 1):
            if row_dim * col_dim == 94:
                for i in range(rows - row_dim + 1):
                    for j in range(cols - col_dim + 1):
                        count += 1
    return count
