import numpy as np
def submatrix_with_n_numbers(arr):
    return sum(1 for i in range(len(arr)-1) for j in range(len(arr[0])-1) if arr[i][j] == 23)
