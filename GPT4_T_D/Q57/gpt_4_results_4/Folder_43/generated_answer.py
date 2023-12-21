
import numpy as np

def submatrix_with_particular_sum(mat):
    results = []
    rows, cols = np.shape(mat)
    for subset_row in range(1, rows+1):
        for subset_col in range(1, cols+1):
            for i in range(rows-subset_row+1):
                for j in range(cols-subset_col+1):
                    subset_mat = mat[i:i+subset_row, j:j+subset_col]
                    if np.sum(subset_mat) == -81:
                        results.append(subset_mat)
    return results
