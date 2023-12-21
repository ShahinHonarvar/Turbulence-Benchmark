
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for i in range(row, rows):
                for j in range(col, cols):
                    submatrix = matrix[row:i+1, col:j+1]
                    if submatrix.size == 8:
                        count += 1
    return count
