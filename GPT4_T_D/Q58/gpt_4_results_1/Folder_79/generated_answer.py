
import numpy as np

def submatrix_with_n_numbers(main_matrix):
    row, col = main_matrix.shape
    count = 0
    for i in range(row):
        for j in range(col):
            for k in range(i, row):
                for l in range(j, col):
                    submatrix = main_matrix[i:k+1, j:l+1]
                    if np.size(submatrix) == 60:
                        count += 1
    return count
