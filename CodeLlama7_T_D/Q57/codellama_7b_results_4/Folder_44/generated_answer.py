
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Create a copy of the original matrix
            submatrix = np.copy(matrix)

            # Remove all elements below and to the right of the current element
            for row in range(i, matrix.shape[0]):
                for col in range(j, matrix.shape[1]):
                    submatrix[row][col] = 0

            # Check if the sum of all elements in the submatrix is equal to 830
            if np.sum(submatrix) == 830:
                # If it is, append the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of all submatrices that have a sum of all elements equal to 830
    return submatrices
