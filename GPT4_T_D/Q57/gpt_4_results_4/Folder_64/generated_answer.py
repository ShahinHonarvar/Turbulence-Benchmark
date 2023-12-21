
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = np.shape(matrix)
    
    submatrices = []
    for submatrix_col_dimension in range(1, cols + 1):
        for submatrix_row_dimension in range(1, rows + 1):
            for i in range(0, rows + 1 - submatrix_row_dimension):
                for j in range(0, cols + 1 - submatrix_col_dimension):
                    submatrix = matrix[i:i + submatrix_row_dimension, j:j + submatrix_col_dimension]
                    if np.sum(submatrix) == -4:
                        submatrices.append(submatrix)
    
    return submatrices
