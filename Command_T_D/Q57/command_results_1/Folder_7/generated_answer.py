import numpy as np
def submatrix_with_particular_sum(matrix):
    result = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if np.sum(matrix[row][:col] + matrix[row][col+1:]) == -128:
                result += [[matrix[row][:col], matrix[row][col+1:]]
    return result
