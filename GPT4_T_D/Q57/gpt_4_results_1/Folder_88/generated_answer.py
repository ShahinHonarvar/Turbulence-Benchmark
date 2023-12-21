
import numpy as np

def submatrix_with_particular_sum(matrix):
    rows, cols = matrix.shape
    sub_matrix_list = []

    for sub_matrix_height in range(1,rows+1):
        for sub_matrix_width in range(1,cols+1):
            for i in range(0,rows-sub_matrix_height+1):
                for j in range(0,cols-sub_matrix_width+1):
                    sub_matrix = matrix[i:i+sub_matrix_height,j:j+sub_matrix_width]
                    if sub_matrix.sum() == -64:
                        sub_matrix_list.append(sub_matrix.tolist())

    return sub_matrix_list
