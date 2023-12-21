
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, columns = matrix.shape
    count = 0
    for i in range(rows):
        for j in range(columns):
            if matrix[i, j] == 175:
                for k in range(i, rows):
                    for l in range(j, columns):
                        submatrix = matrix[i:k+1, j:l+1]
                        if submatrix.size == 175:
                            count += 1
    return count
