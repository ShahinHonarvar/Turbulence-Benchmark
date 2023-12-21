import numpy as np
def submatrix_with_n_numbers(matrix):
    return sum(1 for i in range(len(matrix)) for j in range(len(matrix[0]))) if matrix.shape[0] >= 159 and matrix.shape[1] >= 159 else 0
