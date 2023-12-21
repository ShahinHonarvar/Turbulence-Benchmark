import numpy as np
def submatrix_with_particular_sum(matrix):
    res = []
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            if matrix[i][j] == -46:
                res += [np.array(matrix[i:i+1], dtype=np.int32), np.array(matrix[i:i+1], dtype=np.int32)]
    return res
