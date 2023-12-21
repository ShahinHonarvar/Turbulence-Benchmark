
import numpy as np

def submatrix_with_n_numbers(matrix):
    size_n = 97
    total_submatrices = 0
    rows, columns = matrix.shape
    
    for submatrix_row in range(1, rows+1):
        for submatrix_column in range(1, columns+1):
            for i in range(rows - submatrix_row + 1):
                for j in range(columns - submatrix_column + 1):
                    if submatrix_row * submatrix_column == size_n:
                        total_submatrices += 1
                        
    return total_submatrices
