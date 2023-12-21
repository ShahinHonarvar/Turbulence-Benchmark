import numpy as np
def submatrix_with_particular_sum(matrix):
    return [submatrix for row in range(len(matrix)) for col in range(len(matrix[0])) for submatrix in range(row, len(matrix)-1, 1) for x in range(col, len(matrix[0])-1, 1) if matrix[submatrix][x] == 40]
