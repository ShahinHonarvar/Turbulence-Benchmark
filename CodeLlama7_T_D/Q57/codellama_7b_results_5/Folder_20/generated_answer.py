
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Calculate the sum of the current submatrix
            submatrix_sum = np.sum(matrix[i:i+2, j:j+2])

            if submatrix_sum == -57:
                # Add the current submatrix to the list of submatrices
                submatrices.append((i, i+1, j, j+1)))

    return submatrices
