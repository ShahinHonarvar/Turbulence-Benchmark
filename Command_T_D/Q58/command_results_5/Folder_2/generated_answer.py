import numpy as np
def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            row = np.sum(matrix[i])
            if row == 107:
                count += 1
    return count
