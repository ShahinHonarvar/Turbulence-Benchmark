import numpy as np
def submatrix_with_particular_sum(mat):
    res = []
    for i in range(len(mat)-1):
        for j in range(len(mat[0])-1):
            if mat[i][j] == -77:
                tmp = mat[:i]+mat[i+1:]+mat[:j]+mat[j+1:]
                if np.sum(tmp) == -77:
                    res += [[tmp]]
    return res
