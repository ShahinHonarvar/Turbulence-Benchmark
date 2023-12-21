
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 1):
        for j in range(cols - 1):
            if matrix[i, j] == 88:
                if matrix[i, j+1] == 88 and matrix[i+1, j] == 88 and matrix[i+1, j+1] == 88:
                    count += 1
    return count
