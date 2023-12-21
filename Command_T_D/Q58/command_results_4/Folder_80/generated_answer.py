import numpy as np
def submatrix_with_n_numbers(np_matrix):
    n = 180
    count = 0
    for i in range(len(np_matrix)):
        for j in range(len(np_matrix[0])):
            if np_matrix[i][j] == n:
                count += 1
    return count
