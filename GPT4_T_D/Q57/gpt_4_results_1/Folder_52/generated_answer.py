
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, columns = matrix.shape
    submatrices = []
    for row_size in range(1, rows + 1):
        for column_size in range(1, columns + 1):
            for i in range(rows - row_size + 1):
                for j in range(columns - column_size + 1):
                    submatrix = matrix[i : i + row_size, j : j + column_size]
                    if submatrix.sum() == 100:
                        submatrices.append(submatrix)
    return submatrices
