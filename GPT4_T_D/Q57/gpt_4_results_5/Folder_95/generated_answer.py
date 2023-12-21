
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, columns = matrix.shape
    for submatrix_row in range(1, rows + 1):
        for submatrix_column in range(1, columns + 1):
            for i in range(rows - submatrix_row + 1):
                for j in range(columns - submatrix_column + 1):
                    submatrix = matrix[i: i + submatrix_row, j: j + submatrix_column]
                    if np.sum(submatrix) == 19:
                        submatrices.append(submatrix)
    return submatrices
