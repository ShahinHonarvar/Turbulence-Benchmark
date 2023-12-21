
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            submatrix = matrix[i:, j:]
            if sum(submatrix.flat) == 16:
                result.append(submatrix)
    return result
