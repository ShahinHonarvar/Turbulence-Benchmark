
import numpy as np

def submatrix_with_n_numbers(matrix):
    submatrix_count = 0
    rows, columns = matrix.shape
    for i in range(rows):
        for j in range(columns):
            for m in range(i + 1, rows + 1):
                for n in range(j + 1, columns + 1):
                    submatrix = matrix[i:m, j:n]
                    if submatrix.size == 33:
                        submatrix_count += 1
    return submatrix_count
