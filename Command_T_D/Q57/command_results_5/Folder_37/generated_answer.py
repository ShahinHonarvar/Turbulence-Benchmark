import numpy as np
def submatrix_with_particular_sum(arr):
    return [y for x in range(len(arr)) for y in range(len(arr[x])) if np.sum(arr[x][:y] + arr[x][y+1:]) == -82]
