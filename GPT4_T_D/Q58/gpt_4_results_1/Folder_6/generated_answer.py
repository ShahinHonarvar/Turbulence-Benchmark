
import numpy as np

def submatrix_with_n_numbers(A):
    r, c = A.shape
    count = 0
    for rm in range(1, r + 1):
        for cm in range(1, c + 1):
            for rmx in range(r - rm + 1):
                for cmx in range(c - cm + 1):
                    if np.size(A[rmx:rmx + rm, cmx:cmx + cm]) == 122:
                        count += 1
    return count
