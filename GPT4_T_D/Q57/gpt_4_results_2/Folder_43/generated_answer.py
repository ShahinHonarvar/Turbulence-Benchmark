
import numpy as np

def submatrix_with_particular_sum(matrix):
    all_submatrices = []
    for y1 in range(matrix.shape[0]):
        for x1 in range(matrix.shape[1]):
            for y2 in range(y1, matrix.shape[0]):
                for x2 in range(x1, matrix.shape[1]):
                    submatrix = matrix[y1:y2+1, x1:x2+1]
                    if np.sum(submatrix) == -81:
                        all_submatrices.append(submatrix)
    return all_submatrices
