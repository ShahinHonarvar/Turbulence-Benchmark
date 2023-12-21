
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows - 1):
        for j in range(cols - 1):
            if matrix[i, j] == 144:
                if matrix[i, j+1] == 144 and matrix[i+1, j] == 144 and matrix[i+1, j+1] == 144:
                    count += 1
    return count
