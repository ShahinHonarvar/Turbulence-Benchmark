import numpy as np
def submatrix_with_n_numbers(arr):
    m, n = len(arr), len(arr[0])
    return sum( sum(row == 18) for row in range(n) )
