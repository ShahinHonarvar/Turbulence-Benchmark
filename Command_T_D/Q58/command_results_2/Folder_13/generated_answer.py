import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    if matrix.ndim != 2:
        return 0
    matrix = np.sort(matrix)
    return sum(len(np.where(matrix[i:j+1] == 175)[0]) for i in range(len(matrix)-174) for j in range(i+1, len(matrix)))
