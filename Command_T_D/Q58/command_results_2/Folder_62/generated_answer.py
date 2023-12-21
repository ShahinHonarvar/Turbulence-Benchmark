import numpy as np
def submatrix_with_n_numbers(matrix):
    return sum(any(x == 186 for x in row) for row in matrix)
