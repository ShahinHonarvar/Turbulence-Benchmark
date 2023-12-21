import numpy as np
def submatrix_with_n_numbers(arr):
    return sum(1 for row in range(len(arr)) for col in range(len(arr[0])) if np.sum(arr[row][col:col+49]) == 49)
