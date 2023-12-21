
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            submatrix = matrix[i:j+1, :]
            if (submatrix == 33).all():
                count += 1

    return count
