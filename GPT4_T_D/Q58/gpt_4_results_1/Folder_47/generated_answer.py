
import numpy as np

def submatrix_with_n_numbers(matrix):
    total = 0
    rows, cols = np.shape(matrix)
    for row in range(rows):
        for col in range(cols):
            for r in range(row+1, rows+1):
                for c in range(col+1, cols+1):
                    if (r-row)*(c-col) == 90:
                        total += 1
    return total
