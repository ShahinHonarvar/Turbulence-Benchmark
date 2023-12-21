
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    submatrix_count = 0
    for r in range(rows):
        for c in range(cols):
            for x in range(r + 1, rows + 1):
                for y in range(c + 1, cols + 1):
                    submatrix = matrix[r:x, c:y]
                    if submatrix.size == 69:
                        submatrix_count += 1
    return submatrix_count
