
import numpy as np

def submatrix_with_n_numbers(matrix):
    n = 4
    count = 0
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[0]) - n + 1):
            if all(matrix[i][j] == matrix[i+k][j+l] for k in range(n) for l in range(n)):
                count += 1
    return count
