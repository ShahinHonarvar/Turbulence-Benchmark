import numpy as np
def submatrix_with_n_numbers(matrix):
    m = len(matrix)
    return sum(1 for i in range(m) if len(set(matrix[i])) == 144)
