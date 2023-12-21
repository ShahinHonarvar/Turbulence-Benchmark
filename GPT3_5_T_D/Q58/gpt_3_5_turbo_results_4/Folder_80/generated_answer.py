
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i+1 < len(matrix) and j+1 < len(matrix[i]):
                submatrix = matrix[i:i+2, j:j+2]
                if np.size(submatrix) == 4:
                    count += 1
    return count
