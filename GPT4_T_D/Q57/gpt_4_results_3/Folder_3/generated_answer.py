
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, columns = matrix.shape
    result = []
    for x in range(rows):
        for y in range(columns):
            for i in range(x + 1, rows + 1):
                for j in range(y + 1, columns + 1):
                    submatrix = matrix[x:i, y:j]
                    if np.sum(submatrix) == 54:
                        result.append(submatrix)
    return result
