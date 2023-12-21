
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row_len in range(1,rows+1):
        for col_len in range(1,cols+1):
            submatrix_elements= row_len*col_len
            if  submatrix_elements==107:
                for i in range(rows-row_len+1):
                    for j in range(cols-col_len+1):
                        count+=1
    return count
