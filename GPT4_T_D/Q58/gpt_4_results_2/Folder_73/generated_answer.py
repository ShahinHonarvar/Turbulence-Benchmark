
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for sub_row in range(row+1, matrix.shape[0]+1):
                for sub_col in range(col+1, matrix.shape[1]+1):
                    submatrix = matrix[row:sub_row, col:sub_col]
                    if submatrix.size == 41:
                        count += 1
    return count
