
import numpy as np

def submatrix_with_particular_sum(matrix):
    list_of_submatrices = []
    shape = matrix.shape
    for row in range(shape[0]):
        for col in range(shape[1]):
            for row_1 in range(row, shape[0]):
                for col_1 in range(col, shape[1]):
                    submatrix = matrix[row:row_1+1, col:col_1+1]
                    if np.sum(submatrix) == 38:
                        list_of_submatrices.append(submatrix.tolist())
    return list_of_submatrices
