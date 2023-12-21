
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for row in range(rows):
        for col in range(columns):
            for size in range(min(rows-row, columns-col) + 1):
                submatrix = matrix[row:row+size, col:col+size]
                if np.size(submatrix) == 127:
                    count += 1
    return count
