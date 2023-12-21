import numpy as np
def submatrix_with_particular_sum(matrix):
    res = []
    for i in range(len(matrix)):
        tmp = []
        for j in range(len(matrix[0])):
            tmp.append(matrix[i][j])
        if np.sum(tmp) == 862:
            res.append(tmp)
    return res
