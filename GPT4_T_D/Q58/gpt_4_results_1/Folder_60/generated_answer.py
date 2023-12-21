
import numpy as np

def submatrix_with_n_numbers(mat):
    rows, cols = mat.shape
    count = 0
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            for k in range(rows - i + 1):
                for l in range(cols - j + 1):
                    if np.size(mat[k: k + i, l: l + j]) == 88:
                        count += 1
    return count
