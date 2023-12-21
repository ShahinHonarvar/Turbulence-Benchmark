
import numpy as np

def submatrix_with_n_numbers(matrix):
    rows, columns = matrix.shape
    count = 0

    for i in range(rows):
        for j in range(columns):
            for k in range(i, rows):
                for l in range(j, columns):
                    sub_matrix = matrix[i:k+1, j:l+1]
                    if np.size(sub_matrix) == 180:
                        count += 1

    return count
