
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, columns = matrix.shape
    for submatrix_size in range(1, min(rows, columns) + 1):
        for row in range(rows - submatrix_size + 1):
            for column in range(columns - submatrix_size + 1):
                submatrix = matrix[row:row+submatrix_size, column:column+submatrix_size]
                if np.sum(submatrix) == 77:
                    submatrices.append(submatrix)
    return submatrices
