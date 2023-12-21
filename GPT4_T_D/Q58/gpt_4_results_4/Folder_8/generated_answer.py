
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, columns = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(columns):
            for k in range(1, min(rows - r + 1, columns - c + 1)):
                submatrix = matrix[r:r+k, c:c+k]
                if submatrix.size == 29:
                    count += 1
    return count
