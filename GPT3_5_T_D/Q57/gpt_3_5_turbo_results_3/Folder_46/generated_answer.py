
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrix_list = []
    rows, cols = matrix.shape
    target_sum = 416

    for top in range(rows):
        for bottom in range(top, rows):
            for left in range(cols):
                for right in range(left, cols):
                    submatrix = matrix[top:bottom+1, left:right+1]
                    if np.sum(submatrix) == target_sum:
                        submatrix_list.append(submatrix.tolist())

    return submatrix_list
