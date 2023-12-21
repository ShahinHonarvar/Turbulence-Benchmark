
import numpy as np

def submatrix_with_particular_sum(matrix):
    nrows, ncols = len(matrix), len(matrix[0])
    submatrices = []

    for rstart in range(nrows):
        for rend in range(rstart+1, nrows+1):
            for cstart in range(ncols):
                for cend in range(cstart+1, ncols+1):
                    submatrix = matrix[rstart:rend, cstart:cend]
                    if np.sum(submatrix) == -77:
                        submatrices.append(submatrix)

    return submatrices
