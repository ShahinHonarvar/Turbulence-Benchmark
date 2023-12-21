
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for x in range(i, len(matrix)):
                for y in range(j, len(matrix[0])):
                    submatrix = matrix[i:x+1, j:y+1]
                    if np.count_nonzero(submatrix == 173) == 173:
                        count += 1
    return count
