
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, cols = len(matrix), len(matrix[0])
    count = 0
    for i in range(rows):
        for j in range(cols):
            for k in range(i, rows):
                for l in range(j, cols):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.count_nonzero(submatrix) == 94:
                        count += 1
    return count
