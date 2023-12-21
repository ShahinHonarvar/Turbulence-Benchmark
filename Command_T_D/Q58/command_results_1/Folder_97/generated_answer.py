import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    if len(matrix) < 120:
        return 0
    return sum(sum(matrix[i:j+120]) for i in range(0, len(matrix)-119) for j in range(i, len(matrix)-119))
