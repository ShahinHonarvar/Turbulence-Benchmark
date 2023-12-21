
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            if (matrix[i][j] == 166) and (matrix[i + 1][j] == 166) and (matrix[i][j + 1] == 166) and (matrix[i + 1][j + 1] == 166)):
                count += 1
    return count
