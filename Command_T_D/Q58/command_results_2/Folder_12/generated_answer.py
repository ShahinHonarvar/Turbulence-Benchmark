import numpy as np
def submatrix_with_n_numbers(arr):
    return sum(1 for i in range(len(arr)-45) for j in range(len(arr[0])-45) if arr[i][j:j+46] == np.full(46, 2))
