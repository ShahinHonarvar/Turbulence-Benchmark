
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row_length in range(1, rows+1):
        for col_length in range(1, cols+1):
            if row_length*col_length == 120:
                for row_index in range(rows-row_length+1):
                    for col_index in range(cols-col_length+1):
                        count += 1
    return count
