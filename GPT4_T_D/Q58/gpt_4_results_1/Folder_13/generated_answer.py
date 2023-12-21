
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for x in range(matrix.shape[0]):
        for y in range(matrix.shape[1]):
            for h in range(x+1, matrix.shape[0] + 1):
                for w in range(y+1, matrix.shape[1] + 1):
                    if (h-x) * (w-y) == 175:
                        count += 1
    return count
