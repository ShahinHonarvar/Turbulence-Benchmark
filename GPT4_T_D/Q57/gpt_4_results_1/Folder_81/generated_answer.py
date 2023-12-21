
import numpy as np
from itertools import product

def submatrix_with_particular_sum(mat):
    m, n = mat.shape
    matrix_list = []
    if m < 3:
        return []
    
    for r, c in product(range(m - 2), range(n - 2)):
        submat = mat[r:r + 3, c:c + 3]
        if submat.sum() == -90:
            matrix_list.append(submat)
    return matrix_list
