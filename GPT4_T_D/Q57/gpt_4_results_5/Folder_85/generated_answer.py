
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    target_sum = -87
    submatrices = []

    for submat_row in range(1, rows + 1):
        for submat_col in range(1, cols + 1):

            overlapping_x = rows - submat_row + 1
            overlapping_y = cols - submat_col + 1

            for i in range(0, overlapping_x):
                for j in range(0, overlapping_y):
                    submat = matrix[i: i+ submat_row, j: j+ submat_col]
                    if np.sum(submat) == target_sum:
                        submatrices.append(submat)

    return submatrices
