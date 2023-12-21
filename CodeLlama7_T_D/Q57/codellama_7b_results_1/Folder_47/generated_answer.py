
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Create a copy of the original matrix
            submatrix = np.copy(matrix)

            # Remove the top left element of the submatrix
            submatrix = submatrix[i:, j:]

            # Check if the sum of all elements in the submatrix is equal to 27
            if submatrix.sum() == 27:
                # If the sum is equal to 27, add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of all submatrices that have a sum of all elements equal to 27
    return submatrices
