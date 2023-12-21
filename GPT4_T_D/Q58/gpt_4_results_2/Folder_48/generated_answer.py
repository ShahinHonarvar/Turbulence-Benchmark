
import numpy as np

def submatrix_with_n_numbers(matrix):
    row, column = matrix.shape
    count = 0
    
    for i in range(row):
        for j in range(column):
            for m in range(i + 1, row + 1):
                for n in range(j + 1, column + 1):
                    if np.prod([m - i, n - j]) == 130:
                        count += 1
    return count
