
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize an empty list to store the elements of the submatrix
            submatrix = []

            # Loop through each element of the submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Add the element to the submatrix if it is within the bounds of the matrix
                    if row < matrix.shape[0] and col < matrix.shape[1]:
                        submatrix.append(matrix[row][col])

            # Calculate the sum of all elements in the submatrix
            sum = np.sum(submatrix)

            # Check if the sum equals -59
            if sum == -59:
                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices that have a sum of -59
    return submatrices
