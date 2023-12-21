
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.sum(submatrix == 173) == 173:
                        count += 1
    return count
