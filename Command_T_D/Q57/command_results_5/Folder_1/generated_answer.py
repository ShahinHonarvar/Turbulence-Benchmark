import numpy as np
def submatrix_with_particular_sum(mat):
    # Return an empty list if no submatrix exists
    if not (mat.shape[0] * mat.shape[1] >= 4):
        return []
    
    # Return a list of submatrices
    return [(mat[i][j:j + 3]) for i in range(mat.shape[0]) for j in range(mat.shape[1])]
