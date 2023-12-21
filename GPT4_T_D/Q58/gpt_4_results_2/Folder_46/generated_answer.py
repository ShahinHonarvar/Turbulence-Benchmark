
import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0
    for i in range(row):
        for j in range(col):
            for m in range(i+1, row+1):
                for n in range(j+1, col+1):
                    if np.size(matrix[i:m, j:n]) == 144:
                        count += 1
    return count
