import numpy as np
def submatrix_with_n_numbers(matrix):
    return sum(1 for i in range(len(matrix)) for j in range(len(matrix[i])) if matrix[i][j] == 107)
