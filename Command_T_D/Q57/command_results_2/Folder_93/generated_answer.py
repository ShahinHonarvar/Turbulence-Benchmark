import numpy as np
def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == -65:
                row = []
                for k in range(j, len(matrix[0])):
                    row.append(matrix[i][k])
                result += [[row]]
    return result
