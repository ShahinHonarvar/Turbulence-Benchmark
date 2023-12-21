
import numpy as np

def submatrix_with_particular_sum(matrix):

    submatrix_list = []
    
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for submatrix_row in range(row+1, matrix.shape[0]+1):
                for submatrix_col in range(col+1, matrix.shape[1]+1):
                    submatrix = matrix[row:submatrix_row, col:submatrix_col]
                    if np.sum(submatrix) == 394:
                        submatrix_list.append(submatrix)
    
    return submatrix_list
