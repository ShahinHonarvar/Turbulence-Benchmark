import numpy as np
def submatrix_with_particular_sum(mat):
    mat = np.array(mat)
    return [mat[i:j+1] for i in range(len(mat)) for j in range(i+1, len(mat)) if sum(mat[i:j+1]) == -137]
