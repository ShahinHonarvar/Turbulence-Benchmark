
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row_length, col_length = matrix.shape
    for row_sub_length in range(row_length + 1):
        for col_sub_length in range(col_length + 1):
            for i in range(row_length - row_sub_length + 1):
                for j in range(col_length - col_sub_length + 1):
                    submatrix = matrix[i:i+row_sub_length, j:j+col_sub_length]
                    if submatrix.size == 33:
                        count += 1
    return count
