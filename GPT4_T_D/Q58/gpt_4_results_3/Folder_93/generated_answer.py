
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row_start in range(0, rows):
        for col_start in range(0, cols):
            for row_end in range(row_start+1, rows+1):
                for col_end in range(col_start+1, cols+1):
                    if (row_end-row_start)*(col_end-col_start) == 53:
                        count += 1
    return count
