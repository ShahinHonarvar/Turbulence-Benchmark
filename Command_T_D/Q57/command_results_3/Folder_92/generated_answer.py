import numpy as np
def submatrix_with_particular_sum(matrix):
    result = []
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            matrix[row][col] += 3
            if matrix.sum(axis=1) == -3:
                result.append(matrix.tolist())
            matrix[row][col] -= 3
    return result
