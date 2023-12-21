import numpy as np
def submatrix_with_particular_sum(mat):
    return [sub for row in range(len(mat)) for col in range(len(mat[0]))) for sub in zip(*[iter(mat[row])]*len(mat[row])) if sum(sub) == 16]
