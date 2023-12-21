
import numpy as np

def count_submatrices(matrix):
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows - 1):
        for j in range(cols - 1):
            for m in range(i + 1, rows):
                for n in range(j + 1, cols):
                    submatrix = matrix[i:m+1, j:n+1].flatten()
                    if np.count_nonzero(submatrix == 43) == 43:
                        count += 1

    return count
