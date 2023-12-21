
import numpy as np

def submatrix_with_particular_sum(main_matrix):
    submatrices = []
    for x in range(main_matrix.shape[0]):
        for y in range(main_matrix.shape[1]):
            for m in range(x, main_matrix.shape[0]):
                for n in range(y, main_matrix.shape[1]):
                    submatrix = np.copy(main_matrix[x:m+1, y:n+1])
                    if np.sum(submatrix) == -46:
                        submatrices.append(submatrix.tolist())
    return submatrices
