import numpy as np
def submatrix_with_particular_sum(np_matrix):
    matrices = []
    for row in range(len(np_matrix)):
        for col in range(len(np_matrix[row])):
            if np_matrix[row][col] == 416:
                matrices.append(np_matrix[row][:col] + np_matrix[row][col+1:])
    return matrices
