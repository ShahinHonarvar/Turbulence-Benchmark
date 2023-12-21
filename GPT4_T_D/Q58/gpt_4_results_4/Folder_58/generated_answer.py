
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    num_rows, num_cols = matrix.shape
    for row_length in range(1, num_rows + 1):
        for col_length in range(1, num_cols + 1):
            for i in range(num_rows - row_length + 1):
                for j in range(num_cols - col_length + 1):
                    submatrix = matrix[i:i+row_length,j:j+col_length]
                    if submatrix.size == 185:
                        count += 1
    return count
