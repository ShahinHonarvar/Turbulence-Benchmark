
import numpy as np
def submatrix_with_n_numbers(mat):
    n = 78
    count = 0
    for i in range(len(mat) - n + 1):
        for j in range(len(mat[0]) - n + 1):
            if np.all(np.isin(mat[i:i+n, j:j+n], [78])):
                count += 1
    return count
