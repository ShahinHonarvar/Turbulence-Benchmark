
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            current_sum = 0
            for k in range(i, rows):
                for l in range(j, cols):
                    current_sum += matrix[k][l]
                    if current_sum == -261:
                        return matrix[i:k+1, j:l+1].tolist()
    return []
