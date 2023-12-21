
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the found submatrices
    found_submatrices = []

    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the matrix
        for j in range(len(matrix[0])):
            # Initialize a temporary submatrix with the current row and column
            temp_submatrix = np.array([[matrix[i][j]]])

            # Loop through the remaining rows and columns of the matrix
            for k in range(i+1, len(matrix)):
                for l in range(j+1, len(matrix[0])):
                    # Add the current row and column to the temporary submatrix
                    temp_submatrix = np.concatenate((temp_submatrix, [[matrix[k][l]]]), axis=0)

                    # Check if the sum of all integers in the temporary submatrix is 19
                    if np.sum(temp_submatrix) == 19:
                        # If so, add the temporary submatrix to the list of found submatrices
                        found_submatrices.append(temp_submatrix)

                        # Reset the temporary submatrix for the next iteration
                        temp_submatrix = np.array([[matrix[i][j]]])

    return found_submatrices
