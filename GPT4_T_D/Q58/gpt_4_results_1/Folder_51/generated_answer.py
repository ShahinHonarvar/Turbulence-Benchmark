
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for i in range(rows):
        for j in range(columns):
            for x in range(i, rows):
                for y in range(j, columns):
                    if (x - i + 1) * (y - j + 1) == 95:
                        count += 1
    return count
