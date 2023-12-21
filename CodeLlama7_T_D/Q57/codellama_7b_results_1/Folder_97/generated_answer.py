
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices with sum -617
    submatrices = []

    # Iterate over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Initialize a new submatrix with size (1, 1)
            submatrix = np.array([[matrix[i][j]]]])

            # Check if the sum of all integers in the submatrix equals -617
            if np.sum(submatrix) == -617:
                # Add the submatrix to the list of submatrices with sum -617
                submatrices.append(submatrix)

    # Return the list of all submatrices with sum -617, or an empty list if no such submatrix is found
    return submatrices
