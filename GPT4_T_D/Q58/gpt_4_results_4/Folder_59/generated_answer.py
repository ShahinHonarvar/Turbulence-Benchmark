
import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    rows, cols = matrix.shape
    for width in range(1, cols+1):
        for height in range(1, rows+1):
            for x in range(0, cols-width+1):
                for y in range(0, rows-height+1):
                    submatrix = matrix[y:y+height, x:x+width]
                    if submatrix.size == 76:
                        submatrix_count += 1
    return submatrix_count
