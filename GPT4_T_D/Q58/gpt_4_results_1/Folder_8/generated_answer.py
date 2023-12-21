
import numpy as np

def submatrix_with_n_numbers(matrix):
    
    total_submatrices = 0
    
    if matrix.size < 29:
        return total_submatrices
    
    for rows in range(matrix.shape[0]):
        for columns in range(matrix.shape[1]):
            for r in range(rows, matrix.shape[0]):
                for c in range(columns, matrix.shape[1]):
                    submatrix = matrix[rows:r+1, columns:c+1]
                    if submatrix.size == 29:
                        total_submatrices += 1
                
    return total_submatrices
