import numpy as np
def submatrix_with_n_numbers(arr):
    return sum(1 for r in range(len(arr)-1) for c in range(len(arr[0])-1) if arr[r][c] == arr[r+1][c] == arr[r][c+1] == arr[r+1][c+1])
