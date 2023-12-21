
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = np.shape(matrix)

    for row in range(rows):
        for col in range(cols):
            for size in range(1, min(rows-row, cols-col)+1):
                submatrix = matrix[row:row+size, col:col+size].flatten()
                if len(submatrix) == 38:
                    count += 1

    return count
