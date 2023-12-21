
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            submatrix = matrix[i][j]
            if len(submatrix) == 9:
                count += 1

    return count
