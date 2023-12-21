
import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0 
    for m in range(1, row + 1):
        for n in range(1, col + 1): 
            if m*n == 20:  
                count += (row - m + 1) * (col - n + 1)
    return(count)
