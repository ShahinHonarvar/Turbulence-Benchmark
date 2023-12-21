
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    return len([submatrix for row in matrix for submatrix in itertools.combinations(row, n) if sum(submatrix) == 120])
