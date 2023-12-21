
import numpy as np

def submatrix_with_n_numbers(mat):
    count = 0
    rows, cols = mat.shape
    for x_start in range(rows):
        for y_start in range(cols):
            for x_end in range(x_start, rows):
                for y_end in range(y_start, cols):
                    submat = mat[x_start:x_end+1, y_start:y_end+1]
                    if np.size(submat) == 185:
                        count += 1
    return count
