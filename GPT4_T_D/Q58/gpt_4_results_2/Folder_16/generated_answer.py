
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    total = 0
    for i in range(rows):
        for j in range(cols):
            for p in range(i, rows):
                for q in range(j, cols):
                    if ((p - i + 1) * (q - j + 1)) == 154:
                        total += 1
    return total
