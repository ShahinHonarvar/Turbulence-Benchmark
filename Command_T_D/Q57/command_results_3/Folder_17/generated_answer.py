import numpy as np
def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            temp = np.array(matrix[i])
            temp[j] += 398
            if temp.sum() == 398:
                result.append(matrix[i])
    return result
