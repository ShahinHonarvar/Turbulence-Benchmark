
import numpy as np

def submatrix_with_n_numbers(matrix):
    m, n = matrix.shape
    count = 0
    for sub_m in range(1, m + 1):
        for sub_n in range(1, n + 1):
            if sub_m * sub_n == 127:
                count += (m - sub_m + 1) * (n - sub_n + 1)
    return count
