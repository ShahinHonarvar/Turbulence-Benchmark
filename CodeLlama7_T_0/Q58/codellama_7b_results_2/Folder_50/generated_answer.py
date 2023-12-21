
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix) - 1):
        for j in range(i + 1, len(matrix)):
            if matrix[i].sum() == 40 and matrix[j].sum() == 40:
                count += 1

    return count
