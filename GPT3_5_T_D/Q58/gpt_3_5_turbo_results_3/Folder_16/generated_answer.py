
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    sub_matrix = matrix[i:k+1, j:l+1]
                    if np.sum(sub_matrix) == 154 * sub_matrix.size:
                        count += 1
    return count
