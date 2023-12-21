
import numpy as np

def submatrix_with_particular_sum(matrix):   
    num_rows, num_columns = matrix.shape 
    submatrix_list = []

    for row_len in range (1,num_rows+1):
        for col_len in range (1,num_columns+1):
            for i in range (0,num_rows-row_len+1):
                for j in range (0,num_columns-col_len+1):
                    submatrix = matrix[i:i+row_len,j:j+col_len]
                    if np.sum(submatrix) == 830: 
                        submatrix_list.append(submatrix)

    return submatrix_list
