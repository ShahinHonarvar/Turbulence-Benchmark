
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrix_list = [] 
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            for r in range(row, matrix.shape[0]):
                for c in range(col, matrix.shape[1]):
                    submatrix = matrix[row:r+1, col:c+1]
                    if np.sum(submatrix) == 8:
                        submatrix_list.append(submatrix.tolist())
    return submatrix_list
