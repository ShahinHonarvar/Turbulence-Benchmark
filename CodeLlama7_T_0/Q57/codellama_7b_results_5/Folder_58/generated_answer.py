
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Create a copy of the original matrix
            submatrix = matrix.copy()

            # Remove all elements from the submatrix that are not in the current row and column
            submatrix = submatrix[i:i+1, j:j+1]

            # Check if the sum of all integers in the submatrix is equal to -137
            if np.sum(submatrix) == -137:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of all submatrices that have a sum of -137
    return submatrices
