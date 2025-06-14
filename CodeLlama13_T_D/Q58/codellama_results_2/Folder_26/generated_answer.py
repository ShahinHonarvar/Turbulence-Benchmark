
import numpy as np
def submatrix_with_n_numbers(arr, n):
    rows = len(arr) - 1
    cols = len(arr[0]) - 1
    count = 0
    for i in range(rows+1):
        for j in range(cols+1):
            for k in range(i, rows+1):
                for l in range(j, cols+1):
                    if np.sum(arr[i:k+1, j:l+1]) == n:
                        count += 1
    return count
