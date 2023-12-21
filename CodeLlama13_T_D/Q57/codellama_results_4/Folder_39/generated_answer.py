
import numpy as np
def submatrices_with_particular_sum(matrix):
    rows, cols = matrix.shape
    for i in range(rows-1):
        for j in range(cols-1):
            for m in range(i+1, rows):
                for n in range(j+1, cols):
                    if np.sum(matrix[i:m, j:n]) == 66:
                        return matrix[i:m, j:n].tolist()
    return []
