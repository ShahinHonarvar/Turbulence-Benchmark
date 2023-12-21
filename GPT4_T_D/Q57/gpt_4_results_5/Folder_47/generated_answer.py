
import numpy as np

def submatrix_with_particular_sum(mat):
    output = []
    rows, cols = mat.shape
    for rl in range(1, rows + 1):
        for cl in range(1, cols + 1):
            for r in range(rows - rl + 1):
                for c in range(cols - cl + 1):
                    sub_mat = mat[r:r+rl, c:c+cl]
                    if np.sum(sub_mat) == 27:
                        output.append(sub_mat)
    return output
