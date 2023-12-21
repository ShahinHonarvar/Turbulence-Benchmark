
import numpy as np
def submatrix_with_particular_sum(matrix):
    submatrices = []
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            sum_of_submatrix = np.sum(matrix[i:i+2, j:j+2])
            if sum_of_submatrix == 616:
                submatrices.append([i, i+1, j, j+1])
    return submatrices
