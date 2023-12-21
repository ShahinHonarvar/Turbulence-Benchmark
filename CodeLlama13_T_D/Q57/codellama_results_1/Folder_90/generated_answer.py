
import numpy as np
def submatrix_with_particular_sum(arr):
    rows, cols = arr.shape
    for i in range(rows-1):
        for j in range(cols-1):
            temp_sum = 0
            for k in range(i, rows):
                for l in range(j, cols):
                    temp_sum += arr[k][l]
                if temp_sum == -452:
                    return [arr[i:k+1, j:l+1]]
    return []
