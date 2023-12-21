
import numpy as np
def submatrix_with_n_numbers(mat):
    count = 0
    for i in range(len(mat)-138):
        for j in range(len(mat[0])-138):
            submat = mat[i:i+139,j:j+139]
            if np.count_nonzero(submat) == 139:
                count += 1
    return count
