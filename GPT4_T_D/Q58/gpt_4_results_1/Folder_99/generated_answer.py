
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for row in range(r, rows):
                for col in range(c, cols):
                    if (row-r+1)*(col-c+1) == 146:
                        count += 1
    return count
