
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    sub_matrix_list = []

    # slicing the sub-matrices till the condition meet
    for r1 in range(0, rows):
        for r2 in range(r1+1, rows+1):
            for c1 in range(0,cols):
                for c2 in range(c1+1, cols+1):
                    sub = matrix[r1:r2, c1:c2]
                    if np.sum(sub) == 64:
                        sub_matrix_list.append(sub)
    return sub_matrix_list
