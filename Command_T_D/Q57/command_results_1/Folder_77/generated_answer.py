import numpy as np
def submatrix_with_particular_sum(arr):
    matrix = np.array(arr)
    return [sub for i in range(len(matrix)-1) for j in range(len(matrix[0])-1) for sub in [[arr[i][j], arr[i][j+1], arr[i+1][j], arr[i+1][j+1]] if np.sum(sub) == -336]
