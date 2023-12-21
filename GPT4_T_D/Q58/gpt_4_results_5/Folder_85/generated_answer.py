
import numpy as np
from scipy import signal

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for row in range(rows):
        for col in range(cols):
            for x in range(row, rows):
                for y in range(col, cols):
                    submatrix = matrix[row:x+1, col:y+1]
                    if submatrix.size == 13:
                        count += 1
    return count
