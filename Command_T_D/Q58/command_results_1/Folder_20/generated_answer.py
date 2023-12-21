import numpy as np
def submatrix_with_n_numbers(matrix):
    return sum(
        1
        for row in range(len(matrix[0]))
        for col in range(len(matrix))
        if np.sum(matrix[row][:49]) == 49
    )
