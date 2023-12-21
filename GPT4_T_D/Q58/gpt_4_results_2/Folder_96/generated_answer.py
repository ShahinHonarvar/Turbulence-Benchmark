
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for m in range(1, rows + 1):
        for n in range(1, cols + 1):
            if m*n==20:
                count += (rows - m + 1) * (cols - n + 1)
    return count
