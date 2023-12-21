
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Extract a submatrix from the original matrix
            submatrix = matrix[i:, j:]

            # Check if the sum of all integers in the submatrix equals -936
            if np.sum(submatrix) == -936:
                # If the condition is met, add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of all submatrices that satisfy the condition
    return submatrices
