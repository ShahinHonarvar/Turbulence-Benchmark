
import numpy as np
def submatrix_with_n_numbers(mat):
    n = mat.shape[0] * mat.shape[1]
    count = 0
    for i in range(n - 172):
        for j in range(i + 1, n - 172):
            submatrix = mat[i:j+1, :][:]
            if np.all(submatrix == 173):
                count += 1
    return count
