
import numpy as np

def submatrix_with_n_numbers(mat):
    count = 0
    rows, cols = mat.shape
    for row_dim in range(1, rows + 1):
        for col_dim in range(1, cols + 1):
            if row_dim * col_dim == 8:
                for r in range(0, (rows - row_dim) + 1):
                    for c in range(0, (cols - col_dim) + 1):
                        submat = np.zeros((row_dim, col_dim))
                        for i in range(r, r + row_dim):
                            for j in range(c, c + col_dim):
                                submat[i - r][j - c] = mat[i][j]
                        count += 1
    return count
