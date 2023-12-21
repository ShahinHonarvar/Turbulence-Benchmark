
import numpy as np

def submatrix_with_n_numbers(matrix):
    count_submatrices = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for h in range(i+1, matrix.shape[0]+1):
                for k in range(j+1, matrix.shape[1]+1):
                    submatrix = matrix[i:h, j:k]
                    if len(np.ravel(submatrix)) == 35:
                        count_submatrices += 1
    return count_submatrices
