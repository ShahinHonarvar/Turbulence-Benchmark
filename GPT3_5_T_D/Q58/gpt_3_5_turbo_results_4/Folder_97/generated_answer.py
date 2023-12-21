
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 120:
                count += 1
                if i + 1 < rows and j + 1 < cols and matrix[i+1][j+1] == 120:
                    count += 1
    return count
