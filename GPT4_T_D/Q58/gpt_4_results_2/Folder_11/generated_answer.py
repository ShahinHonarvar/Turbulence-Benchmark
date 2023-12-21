
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row_num, col_num = matrix.shape
    for row_len in range(1,row_num+1):
        for col_len in range(1,col_num+1):
            if row_len*col_len == 38:
                for i in range(row_num-row_len+1):
                    for j in range(col_num-col_len+1):
                        count += 1
    return count
