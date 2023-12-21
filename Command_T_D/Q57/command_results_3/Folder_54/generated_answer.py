import numpy as np
def submatrix_with_particular_sum(matrix):
    return [submatrix for row in range(len(matrix)) for col in range(len(matrix[0])) for submatrix in range(row, len(matrix) - 1, 1) for c in range(col, len(matrix[0]) - 1, 1) if np.sum(matrix[row][:c] + matrix[row][c+1:]] == -59) and np.sum(matrix[submatrix:][:c] + matrix[submatrix:][c+1:]] == -59)]
