
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for x in range(rows):
        for y in range(cols):
            for x2 in range(x, rows):
                for y2 in range(y, cols):
                    submatrix = matrix[x:x2+1, y:y2+1]
                    if np.count_nonzero(submatrix) == 138:
                        count += 1
    return count
