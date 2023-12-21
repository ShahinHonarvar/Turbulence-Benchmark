
import numpy as np

def submatrix_with_n_numbers(arr, n):
    rows, cols = arr.shape
    count = 0
    
    for r in range(rows-n+1):
        for c in range(cols-n+1):
            subarr = arr[r:r+n, c:c+n]
            if np.sum(subarr == n) == n:
                count += 1
    
    return count
