
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for x in range(rows):
        for y in range(columns):
            for m in range(x, rows):
                for n in range(y, columns):
                    if ((m - x + 1) * (n - y + 1)) == 49:
                        count += 1
    return count
