
import numpy as np

def submatrix_with_particular_sum(matrix):
    res = []
    w, h = matrix.shape
    for w_sub in range(1, w + 1):
        for h_sub in range(1, h + 1):
            for i in range(w - w_sub + 1):
                for j in range(h - h_sub + 1):
                    submatrix = matrix[i:i+w_sub, j:j+h_sub]
                    if np.sum(submatrix) == -87:
                        res.append(submatrix)
    return res
