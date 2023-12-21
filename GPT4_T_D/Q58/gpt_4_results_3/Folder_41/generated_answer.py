
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i1 in range(rows):
        for j1 in range(cols):
            for i2 in range(i1, rows):
                for j2 in range(j1, cols):
                    if (i2 - i1 + 1) * (j2 - j1 + 1) == 73:
                        count += 1
    return count
