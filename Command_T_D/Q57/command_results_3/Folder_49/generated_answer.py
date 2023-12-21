import numpy as np
def submatrix_with_particular_sum(np_matrix):
    matrix = np_matrix.tolist()
    return [[x for x in row if x == -42] for row in matrix]
