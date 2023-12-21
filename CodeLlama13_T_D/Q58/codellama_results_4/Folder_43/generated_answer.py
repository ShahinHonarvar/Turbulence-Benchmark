
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    for i in range(rows-7):
        for j in range(cols-7):
            count = 0
            for k in range(8):
                for l in range(8):
                    if matrix[i+k][j+l] == 1:
                        count += 1
            if count == 64:
                return True
    return False
