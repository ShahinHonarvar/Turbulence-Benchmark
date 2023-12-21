
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for sub_r in range(1, rows + 1):
        for sub_c in range(1, cols + 1):
            if sub_r * sub_c == 13:
                count += (rows - sub_r + 1) * (cols - sub_c + 1)
    return count
