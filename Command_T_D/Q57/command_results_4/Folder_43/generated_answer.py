import numpy as np
def submatrix_with_particular_sum(matrix):
    return [submatrix for row in range(len(matrix[0])) for submatrix in range(len(matrix)) if sum(matrix[submatrix][row]) == -81]
