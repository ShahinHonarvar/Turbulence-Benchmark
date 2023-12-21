
import numpy as np

def submatrix_with_n_numbers(mat):
    count = 0
    rows, cols = mat.shape
    for i in range(rows):
        for j in range(cols):
            for x in range(i, rows):
                for y in range(j, cols):
                    submat = mat[i:x+1, j:y+1]
                    if np.size(submat) == 88:
                        count += 1
    return count
