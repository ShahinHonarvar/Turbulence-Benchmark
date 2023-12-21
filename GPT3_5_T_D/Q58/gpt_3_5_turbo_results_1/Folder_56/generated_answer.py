
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0

    for i in range(rows - 1):
        for j in range(cols - 1):
            if matrix[i, j] == 68:
                if matrix[i, j+1] == 68 and matrix[i+1, j] == 68 and matrix[i+1, j+1] == 68:
                    count += 1

    return count
