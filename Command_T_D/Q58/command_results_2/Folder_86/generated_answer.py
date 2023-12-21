import numpy as np
def submatrix_with_n_numbers(mat):
    mat = np.array(mat)
    if len(mat) == 0 or len(mat[0]) == 0:
        return 0
    cnt = 0
    for i in range(len(mat)-1):
        for j in range(len(mat[0])-1):
            cnt += mat[i][j] == 138
            if cnt == 138:
                break
    return cnt
