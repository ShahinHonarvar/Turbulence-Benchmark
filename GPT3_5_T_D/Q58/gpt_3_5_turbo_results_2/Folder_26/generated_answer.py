
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    count = 0

    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 115:
                for k in range(1, rows - i + 1):
                    for l in range(1, cols - j + 1):
                        if k * l == 115:
                            count += 1

    return count
