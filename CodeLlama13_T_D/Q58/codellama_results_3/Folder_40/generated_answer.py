
import numpy as np
def submatrix_with_n_numbers(m):
    n = len(m)
    if n == 0: return 0
    counts = {1: 0, 2: 0}
    for i in range(n):
        for j in range(i+1, n):
            s = np.concatenate([np.flipud(m[i:j]), m[j:]])
            if all(s == 1): counts[1] += 1
            elif all(s != 1) and len(s) > 0: counts[2] += 1
    return counts[1] + counts[2]
