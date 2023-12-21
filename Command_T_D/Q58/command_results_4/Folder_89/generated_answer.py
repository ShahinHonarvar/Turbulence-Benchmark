import numpy as np
def submatrix_with_n_numbers(matrix):
    m = matrix.shape[0]
    n = matrix.shape[1]
    count = 0
    for i in range(m):
        for j in range(n):
            num = 0
            for k in range(18):
                if matrix[i][j] == k + 1:
                    num += 1
            if num == 18:
                count += 1
    return count
