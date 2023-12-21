
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    sub_matrices = []
    
    for i in range(rows):
        for j in range(cols):
            for m in range(i, rows):
                for n in range(j, cols):
                    sub_matrix = matrix[i:m+1, j:n+1]
                    if np.sum(sub_matrix) == -20:
                        sub_matrices.append(sub_matrix.tolist())
    
    return sub_matrices
