
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if i+1 < rows and j+1 < cols:
                submatrix = np.array([[matrix[i, j], matrix[i, j+1]], [matrix[i+1, j], matrix[i+1, j+1]]])
                if np.count_nonzero(submatrix == 37) == 4:
                    count += 1
    return count
