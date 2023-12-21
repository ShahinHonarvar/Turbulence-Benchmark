
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row, col = matrix.shape
    for subRow in range(1,row+1):
        for subCol in range(1,col+1):
            if subRow*subCol == 99:
                count += (row-subRow+1)*(col-subCol+1)
    return count
