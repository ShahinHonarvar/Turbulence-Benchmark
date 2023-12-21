
import numpy as np

def submatrix_with_n_numbers(mat):
    row, col = mat.shape
    count = 0
    for i in range(row):
        for j in range(col):
            for m in range(i+1, row+1):
                for n in range(j+1, col+1):
                    if np.size(mat[i:m, j:n]) == 69:
                        count += 1
    return count
