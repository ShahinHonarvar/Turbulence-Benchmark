import numpy as np
def submatrix_with_n_numbers(mat):
    mat = np.array(mat)
    res = 0
    for i in range(len(mat) - 1):
        for j in range(len(mat[i]) - 1):
            tmp = mat[i][j:j + 191]
            if len(tmp) == 191:
                res += 1
    return res
