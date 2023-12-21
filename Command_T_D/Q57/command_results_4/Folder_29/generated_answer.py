import numpy as np
def submatrix_with_particular_sum(matrix):
    m = len(matrix)
    n = len(matrix[0])
    result = []
    for i in range(m):
        for j in range(n):
            current_sum = 0
            for k in range(i, m):
                current_sum += matrix[k][j]
            if current_sum == 84:
                result += [[matrix[i][j]]]
            elif current_sum < 84:
                break
            else:
                result += [[matrix[i][j], matrix[i][j+1]]
    return result
