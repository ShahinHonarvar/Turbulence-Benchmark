import numpy as np
def submatrix_with_particular_sum(arr):
    matrix = np.array(arr)
    if len(matrix) == 0:
        return []
    if len(matrix[0]) == 0:
        return []
    return [list(row) for row in matrix if len(row) == len(row) and sum(row) == 21]
