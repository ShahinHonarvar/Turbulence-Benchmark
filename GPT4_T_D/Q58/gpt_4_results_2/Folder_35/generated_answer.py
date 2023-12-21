
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for x in range(rows):
        for y in range(cols):
            for submatrix_width in range(1, cols - y + 1): 
                for submatrix_height in range(1, rows - x + 1):
                    if submatrix_width * submatrix_height == 111:
                        count += 1
    return count
