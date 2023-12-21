
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r_start in range(0, rows):
        for c_start in range(0, cols):
            for r_end in range(r_start, rows):
                for c_end in range(c_start, cols):
                    submat = matrix[r_start:r_end+1, c_start:c_end+1]
                    if submat.size == 17:
                        count += 1
    return count
