
import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0
    for i in range(row):
        for j in range(col):
            for m in range(i, row):
                for n in range(j, col):
                    if (m-i+1) * (n-j+1) == 18:
                        count += 1
    return count
