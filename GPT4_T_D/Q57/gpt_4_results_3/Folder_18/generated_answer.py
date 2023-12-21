
import numpy as np

def submatrix_with_sum(matrix, desired_sum):
    rows, columns = matrix.shape
    submatrices = []
    
    for row_start in range(rows):
        for row_end in range(row_start+1, rows+1):
            for col_start in range(columns):
                for col_end in range(col_start+1, columns+1):
                    submatrix = matrix[row_start:row_end, col_start:col_end]
                    if np.sum(submatrix) == desired_sum:
                        submatrices.append(submatrix.tolist())
    return submatrices

def submatrix_with_particular_sum(matrix):
    return submatrix_with_sum(matrix, 616)
