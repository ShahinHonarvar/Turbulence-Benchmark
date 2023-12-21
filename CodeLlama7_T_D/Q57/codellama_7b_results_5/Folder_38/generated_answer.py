
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the output list
    submatrices = []

    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Create a copy of the original matrix
            submatrix = np.copy(matrix)

            # Remove all elements from the submatrix that are not in the current row and column
            submatrix = submatrix[i:, j:]

            # Check if the sum of all integers in the submatrix equals 34
            if np.sum(submatrix) == 34:
                # If so, add the submatrix to the output list
                submatrices.append(submatrix)

    # Return the output list
    return submatrices
