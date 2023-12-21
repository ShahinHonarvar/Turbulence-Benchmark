
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices with the sum equal to -83
    submatrices = []

    # Loop through each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Initialize a list to store the indices of the elements in the submatrix
            indices = []

            # Add the indices of all elements in the submatrix to the list
            for row_index in range(i, i + 3):
                for col_index in range(j, j + 3):
                    if (row_index < matrix.shape[0]) and (col_index < matrix.shape[1]):
                        indices.append((row_index, col_index))

            # If the list of indices is not empty, create a submatrix with the specified sum
            if len(indices) != 0:
                submatrix = np.array([matrix[index][j] for index, j in indices])

                # Check if the sum of all integers in the submatrix is equal to -83
                if np.sum(submatrix) == -83:
                    submatrices.append(submatrix)

    # Return the list of all submatrices with the specified sum
    return submatrices
