
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(1, rows+1):
        for j in range(1, cols+1):
            for row in range(rows - i + 1):
                for col in range(cols - j + 1):
                    submatrix = matrix[row:row+i, col:col+j]
                    if submatrix.size == 29:
                        count += 1
    return count
