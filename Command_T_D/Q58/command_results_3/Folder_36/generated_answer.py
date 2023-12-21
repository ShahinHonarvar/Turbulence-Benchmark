import numpy as np
def submatrix_with_n_numbers(mat):
    mat = np.array(mat)
    mask = np.full(mat.shape, False)
    for i in range(0, len(mat)-130):
        for j in range(0, len(mat[0])-130):
            if mat[i][j] == 131:
                mask[i][j] = True
                mask[i+1:i+130+1][j] = True
                mask[i][j+1:j+130+1] = True
    return mask.sum()
