
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for submatrix_size in range(1, min(rows, cols) + 1):
        for i in range(rows - submatrix_size + 1):
            for j in range(cols - submatrix_size + 1):
                submatrix = matrix[i:i+submatrix_size, j:j+submatrix_size]
                if submatrix.size == 78:
                    count += 1
    return count
