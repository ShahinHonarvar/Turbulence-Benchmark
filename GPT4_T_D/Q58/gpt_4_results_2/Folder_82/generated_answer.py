
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    row, col = matrix.shape
    for i in range(row):
        for j in range(col):
            for x in range(i+1, row+1):
                for y in range(j+1, col+1):
                    submatrix = matrix[i:x, j:y]
                    if np.size(submatrix) == 99:
                        count += 1
    return count
