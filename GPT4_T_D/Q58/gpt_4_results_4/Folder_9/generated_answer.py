
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for p in range(i+1, rows+1):
                for q in range(j+1, cols+1):
                    submatrix = matrix[i:p, j:q]
                    if submatrix.size == 33:
                        count += 1
    return count
