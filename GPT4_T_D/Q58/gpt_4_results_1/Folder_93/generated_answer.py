
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for p in range(i, matrix.shape[0]):
                for q in range(j, matrix.shape[1]):
                    if (p - i + 1) * (q - j + 1) == 53:
                        count += 1
    return count
