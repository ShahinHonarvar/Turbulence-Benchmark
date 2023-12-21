
import numpy as np
def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0] - 89):
        for j in range(matrix.shape[1] - 89):
            if matrix[i:i+95, j:j+95].sum() == 95 * 95:
                count += 1
    return count
