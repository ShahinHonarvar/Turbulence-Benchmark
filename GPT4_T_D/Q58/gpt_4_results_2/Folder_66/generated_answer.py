
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for i in range(rows):
        for j in range(columns):
            for m in range(i, rows):
                for n in range(j, columns):
                    if (m - i + 1) * (n - j + 1) == 42:
                        count += 1
    return count
