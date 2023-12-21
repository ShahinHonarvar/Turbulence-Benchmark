import numpy as np
def submatrix_with_particular_sum(mat):
    rows = mat.shape[0]
    cols = mat.shape[1]
    row_idx = np.random.randint(rows)
    col_idx = np.random.randint(cols)
    row_idx_2 = np.random.randint(rows)
    col_idx_2 = np.random.randint(cols)
    return [(row_idx, row_idx_2, col_idx, col_idx_2)]
