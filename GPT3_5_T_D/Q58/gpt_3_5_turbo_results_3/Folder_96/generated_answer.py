
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            if np.sum(matrix[i:i+2, j:j+2]) == 20:
                count += 1
    return count
