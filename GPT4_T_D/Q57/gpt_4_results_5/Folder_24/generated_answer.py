
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    results = []
    for x1 in range(rows):
        for y1 in range(cols):
            for x2 in range(x1+1, rows+1):
                for y2 in range(y1+1, cols+1):
                    sub_matrix = matrix[x1:x2, y1:y2]
                    if np.sum(sub_matrix) == -36:
                        results.append(sub_matrix.tolist())
    return results
