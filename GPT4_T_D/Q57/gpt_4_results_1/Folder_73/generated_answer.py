
import numpy as np

def submatrix_with_particular_sum(matrix):
    m, n = matrix.shape
    submatrix_list = []

    for submatrix_width in range(1, m+1):
        for submatrix_height in range(1, n+1):
            for i in range(m - submatrix_width + 1):
                for j in range(n - submatrix_height + 1):
                    submatrix = matrix[i:(i+submatrix_width), j:(j+submatrix_height)]
                    if np.sum(submatrix) == 93:
                        submatrix_list.append(submatrix)

    return submatrix_list
