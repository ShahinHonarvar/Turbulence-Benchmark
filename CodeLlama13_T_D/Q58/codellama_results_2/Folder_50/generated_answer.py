
import numpy as np
def submatrix_with_n_numbers(mat):
    n = mat.shape[0] * mat.shape[1]
    if n == 40:
        return 1
    
    count = 0
    for i in range(n-39):
        for j in range(n-39):
            submat = mat[i:i+40, j:j+40]
            if np.sum(submat) == 40:
                count += 1
    
    return count
