
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices_list = []
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for x in range(i, matrix.shape[0]):
                for y in range(j, matrix.shape[1]):
                    submatrix = matrix[i:x + 1, j:y + 1]
                    if submatrix.sum() == 35:
                        submatrices_list.append(submatrix)
    return submatrices_list
