
import numpy as np
def submatrix_with_n_numbers(mat):
    count = 0
    for i in range(len(mat) - 139 + 1):
        for j in range(len(mat[0]) - 139 + 1):
            sub = mat[i:i+139, j:j+139]
            if np.sum(sub == 1) == 139:
                count += 1
    return count
