
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for row in range(rows):
        for col in range(cols):
            for x in range(row+1, rows+1):
                for y in range(col+1, cols+1):
                    submatrix = matrix[row:x, col:y]
                    if submatrix.size == 97:
                        count += 1
    return count
