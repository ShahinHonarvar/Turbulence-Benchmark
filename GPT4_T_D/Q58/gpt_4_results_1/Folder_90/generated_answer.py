
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if i * j == 176:
                count += (rows - i + 1) * (cols - j + 1)
    return count
