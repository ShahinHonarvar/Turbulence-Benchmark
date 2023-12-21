
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape
    for i in range(rows):
        for j in range(cols):
            if j + 1 < cols and i + 1 < rows:
                submatrix = matrix[i:i+2, j:j+2]
                if np.all(submatrix == 46):
                    count += 1
    return count
