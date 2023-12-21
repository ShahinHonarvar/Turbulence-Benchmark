import numpy as np
def submatrix_with_particular_sum(mat):
    if len(mat) == 0:
        return []
    return [mat[i:j] for i in range(0, len(mat)) for j in range(i, len(mat))]
