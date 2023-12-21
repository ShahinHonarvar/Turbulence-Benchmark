
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices_list = []
    rows, cols = matrix.shape
    
    for submatrix_dimen in range(1, min(rows, cols) + 1):
        for i in range(0, rows - submatrix_dimen + 1):
            for j in range(0, cols - submatrix_dimen + 1):
                submatrix = matrix[i : i + submatrix_dimen, j : j + submatrix_dimen]
                if submatrix.sum() == 41:
                    submatrices_list.append(submatrix)
        
    return submatrices_list
