
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    negative_thirty_eight_submatrices = []
    for row in range(rows):
        for col in range(cols):
            for size in range(1, min(rows-row+1, cols-col+1)):
                submatrix = matrix[row:row + size, col:col + size]
                if np.sum(submatrix) == -38:
                    negative_thirty_eight_submatrices.append(submatrix.tolist())
    return negative_thirty_eight_submatrices
