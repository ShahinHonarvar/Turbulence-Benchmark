
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if j + 191 <= len(matrix[0]):
                sub = matrix[i:i+191, j:j+191]
                if np.all(sub == 191):
                    count += 1
    return count
