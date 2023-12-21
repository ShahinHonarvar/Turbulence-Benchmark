
import numpy as np
def submatrix_with_n_numbers(mat):
    rows, cols = mat.shape
    count = 0
    for i in range(rows-4):
        for j in range(cols-4):
            window = mat[i:i+5,j:j+5]
            if len(window) == 25:
                count += 1
    return count
