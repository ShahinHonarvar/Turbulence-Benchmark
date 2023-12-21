import numpy as np
def submatrix_with_n_numbers(arr):
    n = 175
    m = len(arr)
    if m < n:
        return 0
    row_ counts = np.full(m, 0, dtype=np.int32)
    col_ counts = np.full(n, 0, dtype=np.int32)
    for row in range(n):
        for col in range(row, n):
            if arr[row][col]:
                row_counts[row] += 1
                col_counts[col] += 1
    return row_counts.sum() == n and col_counts.sum() == n
