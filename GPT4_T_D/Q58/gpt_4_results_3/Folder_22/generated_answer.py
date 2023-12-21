
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    n_rows, n_cols = matrix.shape
    for i in range(n_rows):
        for j in range(n_cols):
            for x in range(1, n_rows - i + 1):
                for y in range(1, n_cols - j + 1):
                    if x * y == 21:
                        count += 1
    return count
