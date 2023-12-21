
import numpy as np
def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for row in range(rows-1):
        for col in range(cols-1):
            submat = matrix[row:row+2, col:col+2]
            if np.count_nonzero(submat == 2) == 4:
                count += 1
    return count
