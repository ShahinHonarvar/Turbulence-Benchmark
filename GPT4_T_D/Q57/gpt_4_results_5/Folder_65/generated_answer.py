
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    results = []

    for x in range(rows):
        for y in range(cols):
            for w in range(x+1, rows+1):
                for h in range(y+1, cols+1):
                    submatrix = matrix[x:w, y:h]
                    if np.sum(submatrix) == 78:
                        results.append(submatrix)
    return results
