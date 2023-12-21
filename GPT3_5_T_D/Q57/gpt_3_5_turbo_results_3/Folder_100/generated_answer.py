
import numpy as np

def submatrix_with_particular_sum(matrix):
    def submatrix_sum(submatrix):
        return np.sum(submatrix)

    submatrix_list = []
    num_rows, num_cols = matrix.shape
    target_sum = 28

    for i in range(num_rows):
        for j in range(num_cols):
            for k in range(i, num_rows):
                for l in range(j, num_cols):
                    submatrix = matrix[i:k+1, j:l+1]
                    if submatrix_sum(submatrix) == target_sum:
                        submatrix_list.append(submatrix.tolist())

    return submatrix_list
