
import numpy as np
def submatrix_with_n_numbers(mat):
    n = 35
    num_rows, num_cols = mat.shape
    count = 0
    for i in range(num_rows-n+1):
        for j in range(num_cols-n+1):
            submat = mat[i:i+n,j:j+n]
            if np.all(submat == n):
                count += 1
    return count
