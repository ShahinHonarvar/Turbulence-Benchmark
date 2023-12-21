
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Create a submatrix by selecting all elements from the current element to the end of the row and column
            submatrix = matrix[i:, j:]

            # Check if the sum of all elements in the submatrix equals -261
            if np.sum(submatrix) == -261:
                # If the submatrix has a matching sum, add it to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of all submatrices such that the sum of all elements in each submatrix equals -261, or an empty list if no such submatrix is found
    return submatrices
