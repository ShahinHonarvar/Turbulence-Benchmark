
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for w in range(len(matrix) - i):
                for h in range(len(matrix[0]) - j):
                    submatrix = matrix[i:i+w+1, j:j+h+1]
                    if np.count_nonzero(submatrix == 191) == w*h:
                        count += 1
    return count
