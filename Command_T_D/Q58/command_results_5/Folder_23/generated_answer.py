import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    return sum(1 for i in range(len(matrix)-1) if matrix[i][:69] == matrix[i+1][:69] and matrix[i][69:] == matrix[i+1][69:])
