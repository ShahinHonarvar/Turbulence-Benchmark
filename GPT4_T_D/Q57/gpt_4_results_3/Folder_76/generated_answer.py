
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    results = []
    for i in range(rows):
        for j in range(cols):
            for s in range(i+1, rows+1):
                for t in range(j+1, cols+1):
                    submatrix = matrix[i : s, j : t]
                    if np.sum(submatrix) == -255:
                        results.append(submatrix)
    return results
