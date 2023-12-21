
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, columns = matrix.shape
    result = []

    for r in range(rows):
        for c in range(columns):
            for rr in range(r+1, rows+1):
                for cc in range(c+1, columns+1):
                    submatrix = matrix[r:rr, c:cc]
                    if np.sum(submatrix) == -42:
                        result.append(submatrix)

    return result
