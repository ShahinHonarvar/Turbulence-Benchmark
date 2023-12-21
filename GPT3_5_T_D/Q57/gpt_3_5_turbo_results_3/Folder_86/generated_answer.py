
import numpy as np

def submatrix_with_particular_sum(matrix):
    def get_submatrices(matrix):
        submatrices = []
        m, n = matrix.shape
        for i in range(m):
            for j in range(n):
                for k in range(i, m):
                    for l in range(j, n):
                        submatrices.append(matrix[i:k+1, j:l+1])
        return submatrices

    target_sum = -394
    submatrices_with_sum = []
    submatrices = get_submatrices(matrix)
    for submatrix in submatrices:
        if np.sum(submatrix) == target_sum:
            submatrices_with_sum.append(submatrix.tolist())

    return submatrices_with_sum
