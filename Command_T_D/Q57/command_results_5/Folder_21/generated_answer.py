import numpy as np
def submatrix_with_particular_sum(arr):
    return [
        [row[i] for row in arr]
        for i in range(len(arr[0]))
        if sum(row) == -936
    ]
