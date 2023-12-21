
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Create a copy of the original matrix
            current_matrix = np.copy(matrix)

            # Remove the rows and columns that are not included in the submatrix
            current_matrix = current_matrix[i:, j:]

            # Check if the sum of all integers in the submatrix is equal to 862
            if np.sum(current_matrix) == 862:
                # Add the submatrix to the list of submatrices
                submatrices.append(current_matrix)

    # Return the list of all submatrices that satisfy the condition
    return submatrices
