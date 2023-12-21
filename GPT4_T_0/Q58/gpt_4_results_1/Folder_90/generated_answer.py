
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for x in range(row, rows):
                for y in range(col, cols):
                    submatrix = matrix[row:x+1, col:y+1]
                    if submatrix.size == 176:
                        count += 1
    return count
