
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for x in range(row+1, rows+1):
                for y in range(col+1, cols+1):
                    if np.size(matrix[row:x, col:y]) == 91:
                        count += 1
    return count
