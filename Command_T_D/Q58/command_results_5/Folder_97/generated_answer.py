import numpy as np
def submatrix_with_n_numbers(mat):
    return sum(1 for i in range(len(mat)) for j in range(len(mat[i])) if len(set(mat[i][j:j+120])) == 120)
