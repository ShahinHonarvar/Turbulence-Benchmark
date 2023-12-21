import numpy as np
def submatrix_with_n_numbers(mat):
    return sum(1 for i in range(len(mat)-28+1) if np.all(np.sum(mat[i:i+29],axis=1) == 28))
