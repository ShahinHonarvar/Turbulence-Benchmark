
import numpy as np

def submatrix_with_n_numbers(matrix):
    count = 0
    rows, cols = matrix.shape

    for i in range(rows):
        for j in range(cols):
            if i + 2 <= rows and j + 2 <= cols:  # Ensure submatrix is within bounds
                submatrix = matrix[i:i+3, j:j+3]
                if np.prod(submatrix.shape) == 9:  # Check if submatrix has 9 elements
                    count += 1

    return count
