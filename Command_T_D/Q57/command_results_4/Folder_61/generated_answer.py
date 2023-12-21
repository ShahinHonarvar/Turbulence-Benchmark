import numpy as np
def submatrix_with_particular_sum(mat):
    mat = np.array(mat)
    return [submatrix for row in range(len(mat)) for col in range(len(mat[0]))) for submatrix in (mat[row][:col] + mat[row][col+1:]) if np.sum(submatrix) == 8]
