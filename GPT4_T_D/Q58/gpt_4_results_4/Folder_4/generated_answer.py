
import numpy as np

def submatrix_with_n_numbers(arr):

    count = 0 
    rows, cols = arr.shape
    
    for submatrix_row_len in range(1, rows+1):
        for submatrix_col_len in range(1, cols+1):
            if submatrix_row_len*submatrix_col_len == 15:
                for row in range(0, (rows-submatrix_row_len+1)):
                    for col in range(0, (cols-submatrix_col_len+1)):
                        submatrix = arr[row:row+submatrix_row_len, col:col+submatrix_col_len]
                        if submatrix.size == 15:
                            count += 1

    return count
