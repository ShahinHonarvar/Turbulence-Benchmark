
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = np.shape(matrix)
    count = 0
    for x in range(1, rows+1):
        for y in range(1, cols+1):
            if x*y == 28:
                count += (rows - x + 1) * (cols - y + 1)
    return count
