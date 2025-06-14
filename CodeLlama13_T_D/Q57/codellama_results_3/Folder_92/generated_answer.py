
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    for i in range(rows-1):
        for j in range(cols-1):
            sum = 0
            for k in range(i, i+2):
                for l in range(j, j+2):
                    sum += matrix[k][l]
            if sum == -3:
                return [matrix[i:i+2, j:j+2]]
    return []
