import numpy as np
def submatrix_with_particular_sum(matrix):
    matrix = np.array(matrix)
    return [matrix[i:j+1] for i in range(len(matrix)-1) for j in range(i+1, len(matrix))]
