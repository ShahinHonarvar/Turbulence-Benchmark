import numpy as np
def submatrix_with_particular_sum(mat):
    return [mat[i:j+1, i:j+1] for i in range(len(mat)-1) for j in range(i+1, len(mat))]
