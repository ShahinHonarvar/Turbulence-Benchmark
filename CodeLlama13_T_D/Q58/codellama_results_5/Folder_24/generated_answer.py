
import numpy as np
def submatrix_with_n_numbers(arr):
    rows, cols = arr.shape
    count = 0
    for i in range(rows-4):
        for j in range(cols-4):
            if sum([arr[i+k][j+l] for k in range(5) for l in range(5)]) == 51:
                count += 1
    return count
