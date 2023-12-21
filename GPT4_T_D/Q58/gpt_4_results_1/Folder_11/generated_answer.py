
import numpy as np

def submatrix_with_n_numbers(mat):
    rows, cols = mat.shape
    count = 0
    for x_length in range(1, rows+1):
        for y_length in range(1, cols+1):
            if x_length * y_length == 38:
                for x_start in range(0, rows-x_length+1):
                    for y_start in range(0, cols-y_length+1):
                        count += 1
    return count
