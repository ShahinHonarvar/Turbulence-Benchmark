
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    result = []
    for r in range(rows):
        for c in range(cols):
            for rr in range(r, rows):
                for cc in range(c, cols):
                    submatrix = matrix[r:rr+1,c:cc+1]
                    if np.sum(submatrix) == -65:
                        result.append(submatrix.tolist())
    return result
