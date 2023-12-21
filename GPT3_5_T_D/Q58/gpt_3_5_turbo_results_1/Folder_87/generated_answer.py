
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    n = 96

    for i in range(rows):
        for j in range(cols):
            if i + n <= rows and j + n <= cols:
                submatrix = matrix[i:i+n, j:j+n]
                if submatrix.size == n * n:
                    count += 1

    return count
