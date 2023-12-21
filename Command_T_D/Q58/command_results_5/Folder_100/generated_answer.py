import numpy as np
def submatrix_with_n_numbers(matrix):
    matrix = np.array(matrix)
    m, n = len(matrix), len(matrix[0])
    if m < 10 or n < 10:
        return 0
    count = 0
    for i in range(10):
        count += matrix[i][:10].sum()
    return count
