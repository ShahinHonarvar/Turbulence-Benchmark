
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    lst_submatrices = []

    for sub_matrix_size in range(1, min(rows, cols)+1):
        for r in range(rows - sub_matrix_size + 1):
            for c in range(cols - sub_matrix_size + 1):
                sub_matrix = matrix[r:r+sub_matrix_size, c:c+sub_matrix_size]
                if np.sum(sub_matrix) == 78:
                    lst_submatrices.append(sub_matrix)
    
    return lst_submatrices
