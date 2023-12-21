
import numpy as np

def submatrix_with_particular_sum(matrix):
    no_rows, no_columns = matrix.shape
    all_submatrices = []
    for row_length in range(1, no_rows+1):
        for column_length in range(1, no_columns+1):
            for i in range(0, no_rows-row_length+1):
                for j in range(0, no_columns-column_length+1):
                    submatrix = matrix[i:i+row_length, j:j+column_length]
                    if np.sum(submatrix) == 64:
                        all_submatrices.append(submatrix)
    
    return all_submatrices
