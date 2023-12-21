
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []

    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a submatrix with the current element as the first element
            submatrix = np.array([[matrix[i,j]]])

            # Check if the sum of all integers in the submatrix is 13
            if submatrix.sum() == 13:
                # If it is, add the submatrix to the result list
                result.append(submatrix)

    # Return the result list
    return result
