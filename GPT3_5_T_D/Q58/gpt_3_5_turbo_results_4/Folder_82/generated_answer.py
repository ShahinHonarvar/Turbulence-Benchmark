
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape

    for i in range(rows - 1):
        for j in range(cols - 1):
            if matrix[i, j] == 99:
                if (matrix[i + 1 : i + 2, j : j + 2] == 99).all():
                    count += 1

    return count
