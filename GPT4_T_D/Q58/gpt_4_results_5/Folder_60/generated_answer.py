
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for submatrix_size_i in range(i+1, rows+1):
                for submatrix_size_j in range(j+2, cols+1):
                    submatrix = matrix[i:submatrix_size_i, j:submatrix_size_j]
                    if submatrix.size == 88:
                        count += 1
    return count
