import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    if not len(matrix) == len(matrix[0]) == 7:
        return 0
    return sum(1 for i in range(len(matrix)) if all(matrix[i] == j for j in range(len(matrix[i]))))
