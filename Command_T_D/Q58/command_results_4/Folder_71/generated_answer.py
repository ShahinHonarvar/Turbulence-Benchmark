import numpy as np
def submatrix_with_n_numbers(matrix):
    return sum(1 for i in range(len(matrix)) for j in range(len(matrix[0])) if matrix[i][j] == 1 and matrix[i][j+1] == 1 and matrix[i+1][j] == 1 and matrix[i+1][j+1] == 1)
