
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrix_list = []
    rows, cols = matrix.shape

    for r in range(rows):
        for c in range(cols):
            for i in range(rows-r):
                for j in range(cols-c):
                    submatrix = matrix[r:r+i+1, c:c+j+1]
                    if np.sum(submatrix) == -15:
                        submatrix_list.append(submatrix.tolist())

    return submatrix_list
