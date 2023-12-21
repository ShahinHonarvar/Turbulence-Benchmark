
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            if i*j == 10:
                count += (rows - i + 1) * (columns - j + 1)
    return count
