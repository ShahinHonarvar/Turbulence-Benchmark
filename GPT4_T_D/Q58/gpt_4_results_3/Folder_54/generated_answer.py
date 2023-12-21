
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            for q in range(i):
                for w in range(j):
                    if (i - q) * (j - w) == 27:
                        count += 1
    return count
