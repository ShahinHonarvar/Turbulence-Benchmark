
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for row in range(rows):
        for col in range(cols):
            for dim in range(1, min(rows-row, cols-col)+1):
                if dim*dim == 95:
                    count += 1
    return count
