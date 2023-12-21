import numpy as np
def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            current_sum = 0
            for k in range(j, len(matrix[0])):
                current_sum += matrix[i][k]
            if current_sum == 15:
                result.append(matrix[i][:j] + matrix[i][j + 1:])
    return result
