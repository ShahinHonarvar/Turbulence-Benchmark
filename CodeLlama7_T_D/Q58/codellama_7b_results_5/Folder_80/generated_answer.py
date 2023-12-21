
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0
    for i in range(rows - 180 + 1):
        for j in range(cols - 180 + 1):
            if all([matrix[i + k][j + l] == 1 for k in range(180) for l in range(180)])):
                count += 1
    return count
