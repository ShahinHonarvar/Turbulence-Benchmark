
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 7 + 1):
        for j in range(len(matrix[0]) - 7 + 1):
            if all([matrix[i + k][j + l] == 7 for k in range(7) for l in range(7)])):
                count += 1

    return count
