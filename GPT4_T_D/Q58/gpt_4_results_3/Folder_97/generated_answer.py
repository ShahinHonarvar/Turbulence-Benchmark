
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for size in range(1, min(rows - r, cols - c) + 1):
                submatrix = matrix[r:r + size, c:c + size]
                if submatrix.size == 120:
                    count += 1
    return count
