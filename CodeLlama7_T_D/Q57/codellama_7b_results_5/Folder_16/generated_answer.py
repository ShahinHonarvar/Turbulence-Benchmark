
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop through each row of the matrix
    for i in range(len(matrix)):

        # Loop through each column of the matrix
        for j in range(len(matrix[i])):

            # Initialize a new submatrix with the current row and column
            submatrix = np.zeros((len(matrix) - 1, len(matrix[i]) - 1))

            # Populate the submatrix with the appropriate elements from the original matrix
            for row in range(len(submatrix)):
                for col in range(len(submatrix[row]))):
                    submatrix[row][col] = matrix[i + row + 1][j + col + 1]

            # Check if the sum of all integers in the submatrix is equal to -157
            if np.sum(submatrix) == -157:

                # If it is, append the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of all submatrices that meet the condition
    return submatrices
