
import numpy as np

def submatrix_with_n_numbers(matrix, n):
    return len([sub for sub in matrix if len(set(map(tuple, sub))) == n])
