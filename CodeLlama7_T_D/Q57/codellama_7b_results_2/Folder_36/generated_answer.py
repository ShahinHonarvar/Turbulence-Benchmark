
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the result list
    result = []

    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Create a submatrix by selecting all elements that are below and to the right of the current element
            submatrix = matrix[i:, j:]

            # Check if the sum of all elements in the submatrix is equal to -779
            if np.sum(submatrix) == -779:
                result.append(submatrix)

    # Return the list of submatrices that have a sum of -779
    return result
