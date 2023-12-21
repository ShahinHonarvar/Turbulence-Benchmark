
import numpy as np

def submatrix_with_particular_sum(matrix):
    result = []
    rows, cols = matrix.shape
    for rstart in range(rows):
        for rend in range(rstart, rows):
            for cstart in range(cols):
                for cend in range(cstart, cols):
                    submatrix = matrix[rstart:rend+1, cstart:cend+1]
                    if np.sum(submatrix) == -83:
                        result.append(submatrix.tolist())
    return result
