
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for nrow in range(1, rows+1):
        for ncol in range(1, cols+1):
            total_blocks = (rows-nrow+1)*(cols-ncol+1)
            if nrow * ncol == 84:
                count += total_blocks
    return count
