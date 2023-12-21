
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the found submatrices
    found_submatrices = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary submatrix with the current cell as the top-left corner
            temp_submatrix = np.zeros((matrix.shape[0], matrix.shape[1]))
            temp_submatrix[i, j] = 1

            # Loop through each row and column of the temporary submatrix
            for k in range(temp_submatrix.shape[0]):
                for l in range(temp_submatrix.shape[1]):
                    # If the current cell is not within the bounds of the original matrix, skip it
                    if i + k >= matrix.shape[0] or j + l >= matrix.shape[1]:
                        continue

                    # Add the current cell to the temporary submatrix
                    temp_submatrix[k, l] = matrix[i + k, j + l]

            # If the sum of all integers in the temporary submatrix is equal to -64, add it to the found submatrices list
            if np.sum(temp_submatrix) == -64:
                found_submatrices.append(temp_submatrix)

    return found_submatrices
