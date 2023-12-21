
import numpy as np

def submatrix_with_n_numbers(matrix):
    row, col = matrix.shape
    count = 0
    for i in range(row):
        for j in range(col):
            for x in range(i, row):
                for y in range(j, col):
                    submatrix = matrix[i:x+1, j:y+1]
                    if np.size(submatrix) == 186:
                        count += 1
    return count
