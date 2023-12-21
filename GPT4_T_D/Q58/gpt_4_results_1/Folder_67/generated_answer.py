
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for r in range(rows):
        for c in range(cols):
            for dr in range(1, rows+1-r):
                for dc in range(1, cols+1-c):
                    if dr * dc == 43:
                        count += 1
    return count
