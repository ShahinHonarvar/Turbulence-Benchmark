
import numpy as np

def submatrix_with_particular_sum(mat):
    result = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            for k in range(i, len(mat)):
                for l in range(j, len(mat[0])):
                    submat = mat[i:k+1, j:l+1]
                    if np.sum(submat) == 80:
                        result.append(submat)
    return result
