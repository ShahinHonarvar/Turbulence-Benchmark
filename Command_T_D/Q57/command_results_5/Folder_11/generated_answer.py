import numpy as np
def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    if matrix.size == 0:
        return []
    return [[row[i] for row in matrix] for i in range(len(row)) if sum(row) == 38]
