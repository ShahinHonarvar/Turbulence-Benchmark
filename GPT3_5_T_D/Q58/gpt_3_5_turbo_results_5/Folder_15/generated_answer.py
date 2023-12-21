
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape

    for i in range(rows):
        for j in range(cols):
            if i < rows - 1 and j < cols - 1:
                submatrix = matrix[i:i+2, j:j+2]
                if submatrix.size == 4:
                    count += 1

    return count
