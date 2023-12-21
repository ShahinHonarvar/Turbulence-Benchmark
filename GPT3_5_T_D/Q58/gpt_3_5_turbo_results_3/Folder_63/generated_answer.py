
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if i+1 < rows and j+1 < cols:
                submatrix = matrix[i:i+2, j:j+2]
                if np.count_nonzero(submatrix == 57) == 4:
                    count += 1
    return count
