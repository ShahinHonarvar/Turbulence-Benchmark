
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    num_rows, num_cols = matrix.shape
    for i in range(num_rows - 1):
        for j in range(num_cols - 1):
            if matrix[i][j] == 66 and matrix[i+1][j] == 66 and matrix[i][j+1] == 66 and matrix[i+1][j+1] == 66:
                count += 1
    return count
