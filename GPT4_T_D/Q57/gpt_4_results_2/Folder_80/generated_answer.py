
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    row, col = matrix.shape
    for i in range(row):
        for j in range(col):
            for x in range(i+1, row+1):
                for y in range(j+1, col+1):
                    sub_matrix = matrix[i:x, j:y]
                    if sub_matrix.sum() == 245:
                        result.append(sub_matrix)
    return result
