
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the found submatrices
    submatrices = []

    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the current submatrix
            temp_matrix = np.zeros((matrix.shape[0], matrix.shape[1]))

            # Fill the temporary matrix with the current submatrix
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    temp_matrix[k - i][l - j] = matrix[k][l]

            # Check if the sum of all integers in the temporary matrix is equal to 382
            if np.sum(temp_matrix) == 382:
                # If so, add the temporary matrix to the list of found submatrices
                submatrices.append(temp_matrix)

    return submatrices
