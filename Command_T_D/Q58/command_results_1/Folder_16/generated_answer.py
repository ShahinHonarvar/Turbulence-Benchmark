import numpy as np
def submatrix_with_n_numbers(mat):
    return np.sum(mat[::(154 // mat.shape[1])][:154] == np.array(range(0, 154), dtype=np.int32))
