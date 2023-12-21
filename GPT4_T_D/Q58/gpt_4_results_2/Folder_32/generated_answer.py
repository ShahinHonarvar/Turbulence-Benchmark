
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape[0], matrix.shape[1]
    for x1 in range(rows):
        for y1 in range(cols):
            for x2 in range(x1, rows):
                for y2 in range(y1, cols):
                    if (x2 - x1 + 1) * (y2 - y1 + 1) == 103:
                        count += 1
    return count
