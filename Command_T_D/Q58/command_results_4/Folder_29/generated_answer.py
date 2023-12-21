import numpy as np
def submatrix_with_n_numbers(mat):
    mat = np.array(mat)
    m, n = len(mat), len(mat[0])
    count = 0
    for i in range(m):
        for j in range(n):
            for k in range(19):
                if mat[i][j] == k + 1:
                    count += 1
                    break
            else:
                count += 1
                break
    return count
