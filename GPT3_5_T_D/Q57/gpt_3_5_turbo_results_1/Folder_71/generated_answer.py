
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[i])):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.sum(submatrix) == 69:
                        result.append(submatrix.tolist())
    return result
