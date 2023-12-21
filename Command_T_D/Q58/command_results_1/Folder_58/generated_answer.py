import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    return len([x for x in range(len(matrix), 0, -1) if matrix[x] == 185])
