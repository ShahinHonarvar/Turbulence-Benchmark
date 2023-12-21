
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for size in range(1, min(rows - r + 1, cols - c + 1)):
                if size ** 2 == 56:
                    count += 1
    return count
