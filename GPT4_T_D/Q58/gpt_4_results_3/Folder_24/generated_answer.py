
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for subrow in range(row, rows):
                for subcol in range(col, cols):
                    submatrix = matrix[row:subrow+1, col:subcol+1]
                    if submatrix.size == 51:
                        count += 1
    return count
