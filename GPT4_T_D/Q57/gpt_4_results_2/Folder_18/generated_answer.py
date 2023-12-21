
import numpy as np
def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for x in range(rows):
        for y in range(cols):
            for xend in range(x, rows):
                for yend in range(y, cols):
                    submatrix = matrix[x:xend+1, y:yend+1]
                    if np.sum(submatrix) == 616:
                        result.append(submatrix)
    return result
