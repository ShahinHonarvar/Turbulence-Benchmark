
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the found submatrices
    submatrices = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the current submatrix
            temp_matrix = np.zeros((3, 3), dtype=int)

            # Fill the temporary matrix with the elements from the original matrix
            for k in range(3):
                for l in range(3):
                    temp_matrix[k, l] = matrix[i + k, j + l]

            # Check if the sum of all integers in the current submatrix equals 95
            if np.sum(temp_matrix) == 95:
                # If so, add the submatrix to the list of found submatrices
                submatrices.append(temp_matrix)

    # Return the list of found submatrices
    return submatrices
