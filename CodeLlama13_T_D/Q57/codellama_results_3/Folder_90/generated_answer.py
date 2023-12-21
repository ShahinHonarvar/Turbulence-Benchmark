
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the found submatrices
    submatrices = []

    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Calculate the sum of all integers in the current submatrix
            current_sum = np.sum(matrix[i:, j:])

            # If the sum is equal to -452, add the submatrix to the list of found submatrices
            if current_sum == -452:
                submatrices.append((i, j))

    return submatrices
