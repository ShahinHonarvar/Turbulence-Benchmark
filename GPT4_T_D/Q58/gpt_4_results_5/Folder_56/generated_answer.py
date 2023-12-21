
import numpy as np

def submatrix_with_n_numbers(matrix):
    total_count = 0
    row_len, col_len = matrix.shape
    for submatrix_size in range(1, min(row_len, col_len) + 1): 
        for row in range(0, row_len - submatrix_size + 1):
            for col in range(0, col_len - submatrix_size + 1):
                if submatrix_size**2 == 68:
                    total_count += 1
    return total_count
