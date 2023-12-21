
import numpy as np
import itertools

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for r in range(rows):
        for c in range(cols):
            for r_delta in range(rows - r + 1):
                for c_delta in range(cols - c + 1):
                    submatrix = matrix[r:r + r_delta, c:c + c_delta]
                    if submatrix.size == 7:
                        count += 1
    return count
