
import numpy as np

def submatrix_with_n_numbers(matrix):
    count_submatrices = 0 
    for i in range(matrix.shape[0]):
        for j in range(i,matrix.shape[0]):
            for k in range(matrix.shape[1]):
                for l in range(k, matrix.shape[1]):
                    submatrix = matrix[i:j+1,k:l+1]
                    if submatrix.size == 179:
                        count_submatrices += 1 
    return count_submatrices
