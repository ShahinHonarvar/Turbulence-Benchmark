
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row_length = len(matrix)
    if row_length > 0:
        col_length = len(matrix[0])
        for row_count in range(1,row_length + 1):
            for col_count in range(1,col_length + 1):
                for r_init in range(0,row_length - row_count + 1):
                    for c_init in range(0,col_length - col_count + 1):
                        if row_count * col_count == 73:
                            count += 1
    return count
