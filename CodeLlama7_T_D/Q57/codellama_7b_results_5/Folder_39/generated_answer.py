
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices with sum equal to 66
    submatrices = []
    # Iterate over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Extract the submatrix by finding the rows and columns that contain the current index
            submatrix = matrix[i:, j:]
            # Check if the sum of all integers in the submatrix is equal to 66
            if np.sum(submatrix) == 66:
                # If it is, add the submatrix to the list of submatrices with sum equal to 66
                submatrices.append(submatrix)
    # Return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 66. If no such submatrix is found, the function should return an empty list.
    return submatrices
