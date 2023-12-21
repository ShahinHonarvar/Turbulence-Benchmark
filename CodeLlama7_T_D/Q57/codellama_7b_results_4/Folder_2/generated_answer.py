
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a new submatrix with the same size as the original matrix
            submatrix = np.zeros((matrix.shape[0], matrix.shape[1]))

            # Fill the submatrix with the elements from the original matrix that have indices equal to i or j in the current row and column
            submatrix[i, j] = matrix[i, j]

            # Check if the sum of all integers in the submatrix is equal to -863
            if np.sum(submatrix) == -863:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of all submatrices that have a sum equal to -863
    return submatrices
