
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for x in range(1, rows+1):
        for y in range(1, cols+1):
            for row in range(rows-x+1):
                for col in range(cols-y+1):
                    if np.size(matrix[row:row+x, col:col+y]) == 69:
                        count += 1
    return count
