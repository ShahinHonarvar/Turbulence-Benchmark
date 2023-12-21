
import numpy as np

def submatrix_with_particular_sum(matrix):
    possible_submatrices = []
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for size in range(1, min(matrix.shape[0] - row, matrix.shape[1] - col) + 1):
                submatrix = matrix[row:row+size, col:col+size]
                if np.sum(submatrix) == -9:
                    possible_submatrices.append(submatrix)
    return possible_submatrices
