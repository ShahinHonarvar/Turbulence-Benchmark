
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for h in range(row, rows):
                for w in range(col, cols):
                    submatrix = matrix[row:h+1, col:w+1]
                    if submatrix.size == 24:
                        count += 1
    return count
