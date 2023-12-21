import numpy as np
def submatrix_with_particular_sum(matrix):
    return [np.array(matrix[i:j+1]) for i in range(len(matrix)-1) for j in range(i+1, len(matrix))]
