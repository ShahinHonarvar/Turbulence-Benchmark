
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)-5):
        for j in range(len(matrix[0])-5):
            sub_matrix = matrix[i:i+6, j:j+6]
            if np.size(sub_matrix) == 60:
                count += 1
    return count
