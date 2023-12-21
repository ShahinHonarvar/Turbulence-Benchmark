
import numpy as np

def submatrix_with_n_numbers(mat):
    rows, cols = np.shape(mat)
    count = 0
    for r_start in range(rows):
        for c_start in range(cols):
            for r_end in range(r_start, rows):
                for c_end in range(c_start, cols):
                    sub_matrix = mat[r_start:r_end+1, c_start:c_end+1]
                    if sub_matrix.size == 144:
                        count += 1
    return count
