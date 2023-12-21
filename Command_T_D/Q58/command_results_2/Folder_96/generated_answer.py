import numpy as np
def submatrix_with_n_numbers(matrix):
    return sum(1 for i in range(len(matrix)-19) for j in range(len(matrix[0])-19) if matrix[i][j:j+20].sum() == 20)
