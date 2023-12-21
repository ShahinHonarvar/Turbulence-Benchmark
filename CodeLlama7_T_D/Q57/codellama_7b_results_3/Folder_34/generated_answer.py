
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Calculate the sum of all integers in the current submatrix
            submatrix_sum = np.sum(matrix[i:i+2, j:j+2])

            if submatrix_sum == -13:
                # Add the current submatrix to the list of submatrices
                submatrices.append(matrix[i:i+2, j:j+2])

    return submatrices
