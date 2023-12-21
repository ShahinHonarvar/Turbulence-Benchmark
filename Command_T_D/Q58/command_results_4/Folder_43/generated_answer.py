import numpy as np
def submatrix_with_n_numbers(arr):
    matrix = np.array(arr)
    return sum(1 for i in range(len(matrix)) for j in range(len(matrix[0])) if (len(set(matrix[i])) == 85) and (len(set(matrix[i])) == 85))
