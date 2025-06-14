
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Iterate over each row and column of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Get the sum of all integers in the current submatrix
            submatrix_sum = np.sum(matrix[i:, j]) + np.sum(matrix[i, j:]) - matrix[i, j]
            # If the sum is equal to -811, add the submatrix to the list of submatrices
            if submatrix_sum == -811:
                submatrices.append((i, j)))

    # Return the list of submatrices that satisfy the condition
    return submatrices
