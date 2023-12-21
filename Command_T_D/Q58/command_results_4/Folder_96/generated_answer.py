import numpy as np
def submatrix_with_n_numbers(arr):
    return sum(1 for i in range(len(arr)) for j in range(i+1,len(arr)) if arr[i][j] == i+j)
