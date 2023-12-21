
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, columns = matrix.shape
    for r in range(rows):
        for c in range(columns):
            for i in range(1, rows-r+1):
                for j in range(1, columns-c+1):
                    submatrix = matrix[r:r+i, c:c+j]
                    if np.count_nonzero(submatrix == 159) == i * j:
                        count += 1
    return count
