
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(1, rows + 1):
        for col in range(1, cols + 1):
            if (row * col == 40):
                count += (rows - row + 1) * (cols - col + 1)
    return count
