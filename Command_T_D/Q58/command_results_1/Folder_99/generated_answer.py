import numpy as np
def submatrix_with_n_numbers(matrix):
    return sum(1 for row in matrix if len(set(row)) == 146)
