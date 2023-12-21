import numpy as np
def submatrix_with_particular_sum(matrix):
    res = []
    for i in range(len(matrix)):
        row = np.array(matrix[i])
        for j in range(len(row)):
            tmp = np.array(row[:j] + row[j+1:])
            if np.sum(tmp) == 411:
                res.append(tmp)
    return res
