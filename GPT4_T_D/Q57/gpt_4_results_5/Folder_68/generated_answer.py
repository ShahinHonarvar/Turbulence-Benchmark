
import numpy as np

def submatrix_with_particular_sum(matrix):
    sub_matrices = []
    
    rows, cols = matrix.shape
    
    #Creating all possible submatrices
    for row_end in range(1, rows + 1):
        for col_end in range(1, cols + 1):
            for row_start in range(row_end):
                for col_start in range(col_end):
                    sub_matrix = matrix[row_start:row_end, col_start:col_end]
                    
                    if np.sum(sub_matrix) == 3:
                        sub_matrices.append(sub_matrix.tolist())
                        
    return sub_matrices
