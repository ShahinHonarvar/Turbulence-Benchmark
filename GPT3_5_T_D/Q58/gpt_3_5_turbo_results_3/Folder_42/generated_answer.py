
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if matrix[i, j] == 193:
                count += 1
                for k in range(i+1, rows):
                    for l in range(j+1, cols):
                        if matrix[k, l] == 193 and (k-i+1)*(l-j+1) == 193:
                            count += 1
    return count
