
import numpy as np

def submatrix_with_particular_sum(mat):
    rows, cols = mat.shape
    sub_matrices = []
    for size in range(1, min(rows, cols)+1):
        for x in range(0, rows - size + 1):
            for y in range(0, cols - size + 1):
                submat = mat[x:x + size, y:y + size]
                if np.sum(submat) == -255:
                    sub_matrices.append(submat)
    return sub_matrices
