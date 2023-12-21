
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 1):
        for j in range(i + 1, len(matrix)):
            if matrix[i].all() == 23 and matrix[j].all() == 23:
                count += 1

    return count
