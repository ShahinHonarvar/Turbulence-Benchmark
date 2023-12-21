
import numpy as np

def submatrix_with_particular_sum(mat):
    result = []
    rows, cols = mat.shape
    for sub_rows in range(1, rows+1):
        for sub_cols in range(1, cols+1):
            for i in range(rows+1-sub_rows):
                for j in range(cols+1-sub_cols):
                    submat = mat[i:i+sub_rows, j:j+sub_cols]
                    if np.sum(submat) == 87:
                        result.append(submat)
    return result
