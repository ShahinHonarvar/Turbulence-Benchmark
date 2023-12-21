
import numpy as np

def submatrix_with_n_numbers(matrix):
    return len([submatrix for submatrix in matrix if 42 in submatrix])
