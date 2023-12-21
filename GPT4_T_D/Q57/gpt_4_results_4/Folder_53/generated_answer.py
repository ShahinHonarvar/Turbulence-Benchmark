
import numpy as np

def submatrix_with_particular_sum(input_matrix):
    m, n = input_matrix.shape
    result = []

    for rowLen in range(1, m+1):
        for columnLen in range(1, n+1):
            for r in range(m-rowLen+1):
                for c in range(n-columnLen+1):
                    submatrix = input_matrix[r:r+rowLen, c:c+columnLen]
                    if np.sum(submatrix) == -37:
                        result.append(submatrix)

    return result
