import numpy as np
def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    if matrix.size == 0:
        return []
    result = []
    for i in range(len(matrix[0])-1):
        for j in range(len(matrix)-1):
            if matrix[i][j] == 8:
                submatrix = matrix[i][j:j+2] + matrix[i+1:i+2] + matrix[j:j+2] + matrix[i:i+1] + matrix[j+1:j+2]
                result.append(submatrix)
    return result
