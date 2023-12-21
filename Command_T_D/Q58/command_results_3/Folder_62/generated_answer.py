import numpy as np
def submatrix_with_n_numbers(arr):
    return sum(1 for row in range(len(arr)) if len(set(arr[row])) == 186)
