
import numpy as np

def submatrix_with_particular_sum(matrix):
    submatrices_list = []
    row_num = len(matrix)
    col_num = len(matrix[0])
    for i in range(row_num):
        for j in range(col_num):
            for k in range(i, row_num):
                for l in range(j, col_num):
                    sub_matrix = matrix[i:k+1, j:l+1]
                    if np.sum(sub_matrix) == 17:
                        submatrices_list.append(sub_matrix.tolist())
    return submatrices_list
