
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for size in range(min(rows-row, cols-col)+1):
                submatrix = matrix[row:row+size, col:col+size]
                if submatrix.size == 45:
                    count += 1
    return count
