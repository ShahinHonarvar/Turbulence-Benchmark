
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, columns = matrix.shape
    submatrices = []
    
    for sub_matrix_size in range(1, min(rows, columns) + 1):
        for x in range(rows - sub_matrix_size + 1):
            for y in range(columns - sub_matrix_size + 1):
                submatrix = matrix[x: x + sub_matrix_size, y: y + sub_matrix_size]
                if np.sum(submatrix) == 27:
                    submatrices.append(submatrix)

    return submatrices
