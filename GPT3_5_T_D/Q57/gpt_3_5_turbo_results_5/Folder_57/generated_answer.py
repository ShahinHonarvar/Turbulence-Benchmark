
import numpy as np

def submatrix_with_particular_sum(matrix):
    def check_submatrix(submatrix):
        return np.sum(submatrix) == 13

    result = []
    rows, cols = matrix.shape

    for i in range(rows):
        for j in range(cols):
            for k in range(i + 1, rows + 1):
                for l in range(j + 1, cols + 1):
                    submatrix = matrix[i:k, j:l]
                    if check_submatrix(submatrix):
                        result.append(submatrix.tolist())

    return result
