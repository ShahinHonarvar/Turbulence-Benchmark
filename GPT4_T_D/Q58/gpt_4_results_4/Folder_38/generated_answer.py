
import numpy as np

def submatrix_with_n_numbers(mat):
    if not isinstance(mat, np.ndarray):
        return 0
    count = 0
    for r in range(1, mat.shape[0] + 1):
        for c in range(1, mat.shape[1] + 1):
            for i in range(mat.shape[0] - r + 1):
                for j in range(mat.shape[1] - c + 1):
                    if r * c == 34:
                        count += 1
    return count
