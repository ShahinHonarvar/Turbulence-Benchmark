import numpy as np
def submatrix_with_particular_sum(matrix):
    return [submatrix for i in range(len(matrix)-1) for j in range(len(matrix[0])-1) for submatrix in matrix[i][:j] + matrix[i][j+1:]]
