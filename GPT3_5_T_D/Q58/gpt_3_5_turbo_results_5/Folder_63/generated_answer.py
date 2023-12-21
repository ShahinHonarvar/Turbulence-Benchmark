
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = len(matrix), len(matrix[0])
    for i in range(rows):
        for j in range(columns):
            for k in range(i, rows):
                for l in range(j, columns):
                    submatrix = matrix[i:k+1, j:l+1]
                    if np.count_nonzero(submatrix == 57) == 57:
                        count += 1
    return count
