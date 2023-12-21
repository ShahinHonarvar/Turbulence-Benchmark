
import numpy as np

def submatrix_with_particular_sum(matrix):
    subs = []
    rows, cols = matrix.shape

    for x in range(rows):
        for y in range(cols):
            for i in range(x+1, rows+1):
                for j in range(y+1, cols+1):
                    sub = matrix[x:i, y:j]
                    if np.sum(sub) == -4:
                        subs.append(sub.tolist())
    return subs
