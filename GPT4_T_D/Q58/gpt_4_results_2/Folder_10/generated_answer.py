
import numpy as np

def submatrix_with_n_numbers(arr):
    rows, cols = arr.shape
    count = 0
    for m in range(1, rows + 1):
        for n in range(1, cols + 1):
            if m * n == 56:
                count += (rows - m + 1) * (cols - n + 1)
    return count
