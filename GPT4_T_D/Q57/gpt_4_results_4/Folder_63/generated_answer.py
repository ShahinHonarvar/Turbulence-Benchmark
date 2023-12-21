
import numpy as np

def submatrix_with_particular_sum(matrix):
    row_length = len(matrix)
    column_length = len(matrix[0])
    submatrices_list = []
    
    for i in range(row_length):
        for j in range(column_length):
            for k in range(i, row_length):
                for l in range(j, column_length):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.sum(submatrix) == 64:
                        submatrices_list.append(submatrix)
    
    return submatrices_list
