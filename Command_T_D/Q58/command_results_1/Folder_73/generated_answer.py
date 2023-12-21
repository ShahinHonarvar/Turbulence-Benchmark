import numpy as np
def submatrix_with_n_numbers(matrix):
    res = 0
    for i in range(len(matrix)-40):
        for j in range(len(matrix[i])-40):
            if matrix[i][j:j+40] == np.full(40, True):
                res += 1
    return res
