
import numpy as np

def submatrix_with_n_numbers(matrix):
    total_submatrices = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for r in range(i + 1, rows + 1):
                for c in range(j + 1, cols + 1):
                    elements = matrix[i:r, j:c].size
                    if elements == 54:
                        total_submatrices += 1
    return total_submatrices
