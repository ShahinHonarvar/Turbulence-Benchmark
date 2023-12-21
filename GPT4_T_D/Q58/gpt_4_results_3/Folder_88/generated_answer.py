
import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for sm in range(1, m+1):
        for sn in range(1, n+1):
            if sm * sn == 67:
                for r in range(m - sm + 1):
                    for c in range(n - sn + 1):
                        count += 1                        
    return count if count > 0 else 0
