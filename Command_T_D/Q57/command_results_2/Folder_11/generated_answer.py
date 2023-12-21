import numpy as np
def submatrix_with_particular_sum(mat):
    m = len(mat)
    n = len(mat[0])
    if m < 2 or n < 2:
        return []
    #your code here
    return [mat[i:j+1, i:j+1].tolist() for i in range(0, m-1) for j in range(0, n-1)]
