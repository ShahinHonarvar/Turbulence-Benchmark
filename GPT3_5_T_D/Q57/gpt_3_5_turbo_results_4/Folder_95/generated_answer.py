
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrix_list = []
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            for m in range(i + 1, rows + 1):
                for n in range(j + 1, cols + 1):
                    submatrix = matrix[i:m, j:n]
                    if np.sum(submatrix) == 19:
                        submatrix_list.append(submatrix.tolist())
    return submatrix_list
