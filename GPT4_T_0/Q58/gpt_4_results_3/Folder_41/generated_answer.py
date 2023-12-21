
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for r in range(row, rows):
                for c in range(col, cols):
                    submatrix = matrix[row:r+1, col:c+1]
                    if submatrix.size == 73:
                        count += 1
    return count
