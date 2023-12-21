
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for row in range(rows):
        for col in range(cols):
            for height in range(1, rows-row+1):
                for width in range(1, cols-col+1):
                    if height * width == 64:
                        count += 1
    return count
