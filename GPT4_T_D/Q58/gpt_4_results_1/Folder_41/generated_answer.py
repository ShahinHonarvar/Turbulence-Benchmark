
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for p in range(i+1, matrix.shape[0]+1):
                for q in range(j+1, matrix.shape[1]+1):
                    submatrix = matrix[i:p, j:q]
                    if np.size(submatrix) == 73:
                        count += 1
    return count
