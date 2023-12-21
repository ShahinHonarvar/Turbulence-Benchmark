
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for i in range(rows):
        for j in range(columns):
            for p in range(i, rows):
                for q in range(j, columns):
                    submatrix = matrix[i: p + 1, j: q + 1]
                    if np.size(submatrix) == 103:
                        count += 1
    return count
