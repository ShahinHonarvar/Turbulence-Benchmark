
import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 120
    count = 0
    rows, cols = matrix.shape
    for r_size in range(1, rows + 1):
        for c_size in range(1, cols + 1):
            if r_size * c_size == n:
                count += (rows - r_size + 1) * (cols - c_size + 1)
    return count
