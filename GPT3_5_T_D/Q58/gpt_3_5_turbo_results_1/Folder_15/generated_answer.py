
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row, col = matrix.shape
    for i in range(row):
        for j in range(col):
            if i + 1 < row and j + 1 < col and len(np.unique(matrix[i:i+2, j:j+2])) == 2:
                count += 1
    return count
