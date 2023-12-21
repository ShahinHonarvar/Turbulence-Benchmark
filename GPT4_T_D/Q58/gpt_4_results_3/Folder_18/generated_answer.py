
import numpy as np

def submatrix_with_n_numbers(arr):
    rows, cols = arr.shape
    counter = 0
    for sub_matrix_row in range(rows):
        for sub_matrix_col in range(cols):
            for sub_matrix_hight in range(sub_matrix_row+1, rows+1):
                for sub_matrix_width in range(sub_matrix_col+1, cols+1):
                    sub_matrix = arr[sub_matrix_row:sub_matrix_hight, sub_matrix_col:sub_matrix_width]
                    if sub_matrix.size == 104:
                        counter += 1
    return counter
