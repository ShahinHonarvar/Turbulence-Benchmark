
import numpy as np

def submatrix_with_n_numbers(matrix):
    total = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for k in range(rows-i+1):
                for l in range(cols-j+1):
                    if k*l == 15:
                        total += 1
    return total
