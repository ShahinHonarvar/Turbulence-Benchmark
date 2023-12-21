import numpy as np
def submatrix_with_n_numbers(arr):
    mat = np.matrix(arr)
    count = 0
    for i in range(len(mat)-2):
        for j in range(len(mat)-2):
            a = mat[i][j]
            b = mat[i+1][j]
            c = mat[i+2][j]
            d = mat[i][j+1]
            e = mat[i+1][j+1]
            f = mat[i+2][j+1]
            count += (a == b == c == d == e == f == 66)
    return count
