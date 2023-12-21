
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(cols):
            for i_end in range(i, rows):
                for j_end in range(j, cols):
                    submatrix = matrix[i:i_end+1, j:j_end+1]
                    if submatrix.size == 48:
                        count += 1
    return count
