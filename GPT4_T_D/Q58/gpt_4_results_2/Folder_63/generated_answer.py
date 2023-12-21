
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for i in range(rows):
        for j in range(columns):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, columns + 1):
                    submatrix = matrix[i:k, j:l]
                    if np.size(submatrix) == 57:
                        count += 1
    return count
