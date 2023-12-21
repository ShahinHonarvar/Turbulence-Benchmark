
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            if matrix[i, j] == 115:
                submatrix = np.array([[matrix[i, j], matrix[i, j + 1]], [[matrix[i + 1, j], matrix[i + 1, j + 1]]]])
                if submatrix.sum() == 230:
                    count += 1

    return count
