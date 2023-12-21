
import numpy as np

def submatrix_with_n_numbers(input_matrix):
    row, col = np.shape(input_matrix)
    count = 0

    for sub_row  in range(1,row+1):
        for sub_col in range(1,col+1):

            if sub_row*sub_col == 42:
                count += (row-sub_row+1)*(col-sub_col+1)
                
    return count
