import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    count = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            temp = matrix[row][col]
            count += temp == 33
            matrix[row][col] = 1
    return count
