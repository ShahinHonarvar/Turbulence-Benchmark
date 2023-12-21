
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for a in range(rows):
        for b in range(a+1, rows+1):
            for c in range(cols):
                for d in range(c+1, cols+1):
                    submatrix = matrix[a:b, c:d]
                    if submatrix.size == 92:
                        count += 1
    return count
