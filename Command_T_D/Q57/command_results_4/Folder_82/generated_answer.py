import numpy as np
def submatrix_with_particular_sum(np_matrix):
    result = []
    for i in range(len(np_matrix)-1):
        for j in range(len(np_matrix[0])-1):
            if np_matrix[i][j] == -27:
                submatrix = np_matrix[i][j:] + np_matrix[i+1:][:j] + np_matrix[i+1:][j+1:]
                if submatrix.shape[0] == submatrix.shape[1] == 3:
                    result.append(submatrix)
    return result
