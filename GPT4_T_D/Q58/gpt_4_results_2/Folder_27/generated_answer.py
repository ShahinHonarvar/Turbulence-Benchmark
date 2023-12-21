
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row_length in range(1, rows+1):
        for col_length in range(1, cols+1):
            for row in range(0, rows-row_length+1):
                for col in range(0, cols-col_length+1):
                    submatrix = matrix[row:row+row_length, col:col+col_length]
                    if submatrix.size == 77:
                        count += 1
    return count
