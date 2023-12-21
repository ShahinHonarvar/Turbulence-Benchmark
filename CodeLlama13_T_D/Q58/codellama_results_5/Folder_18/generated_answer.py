
import numpy as np

def submatrix_with_n_numbers(matrix):
    return len([row for row in matrix if row.count(104) == 104])
