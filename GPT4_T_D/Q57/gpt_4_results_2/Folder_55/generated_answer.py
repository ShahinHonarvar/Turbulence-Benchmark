
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    M = len(matrix)
    N = len(matrix[0])
    for sub_size in range(1, min(M, N) + 1):
        for row in range(M - sub_size + 1):
            for col in range(N - sub_size + 1):
                submatrix = matrix[row:row+sub_size, col:col+sub_size]
                if np.sum(submatrix) == 1:
                    result.append(submatrix.tolist())
    return result
