
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices = []
    rows, columns = np.shape(matrix)
    for row_start in range(rows):
        for column_start in range(columns):
            for row_end in range(row_start, rows):
                for column_end in range(column_start, columns):
                    submatrix = matrix[row_start:row_end+1, column_start:column_end+1]
                    if np.sum(submatrix) == 2:
                        submatrices.append(submatrix.tolist())
    return submatrices
