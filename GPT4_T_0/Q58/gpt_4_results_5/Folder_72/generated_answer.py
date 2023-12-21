
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for x in range(i, rows):
                for y in range(j, cols):
                    if (x - i + 1) * (y - j + 1) == 16:
                        count += 1
    return count
