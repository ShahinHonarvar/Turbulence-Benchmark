
import numpy as np
def submatrix_with_n_numbers(matrix):
    rows, cols = matrix.shape
    for i in range(rows-6):
        for j in range(cols-6):
            submat = matrix[i:i+7, j:j+7]
            if (submat == 77).all():
                return True
    return False
