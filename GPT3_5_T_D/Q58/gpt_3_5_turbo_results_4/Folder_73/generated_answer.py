
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)-3):
        for j in range(len(matrix[0])-3):
            submatrix = matrix[i:i+4, j:j+4]
            if np.count_nonzero(submatrix == 41) == 16:
                count += 1
    return count
