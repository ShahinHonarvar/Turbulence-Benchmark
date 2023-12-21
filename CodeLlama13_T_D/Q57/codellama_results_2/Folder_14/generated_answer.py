
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []

    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary submatrix with the current cell as the top-left corner
            temp = matrix[i:, j:]

            # Check if the sum of all integers in the temporary submatrix equals -93
            if np.sum(temp) == -93:
                # If so, add the submatrix to the result list
                result.append(temp)

    # Return the result list
    return result
