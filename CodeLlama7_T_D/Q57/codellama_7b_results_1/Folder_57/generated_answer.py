
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the output list
    output = []
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Create a submatrix with only the element at (i,j)
            submatrix = matrix[i:i+1, j:j+1]
            # Check if the sum of all elements in the submatrix is equal to 13
            if np.sum(submatrix) == 13:
                # If it is, add it to the output list
                output.append(submatrix)
    # Return the output list
    return output
