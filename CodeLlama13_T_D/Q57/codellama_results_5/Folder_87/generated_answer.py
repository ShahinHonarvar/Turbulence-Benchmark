
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the found submatrices
    submatrices = []

    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a 2D numpy array to store the current submatrix
            current_submatrix = np.zeros((3, 3), dtype=np.int)

            # Fill the current submatrix with the elements of the input matrix
            for k in range(current_submatrix.shape[0]):
                for l in range(current_submatrix.shape[1]):
                    if i + k < matrix.shape[0] and j + l < matrix.shape[1]:
                        current_submatrix[k, l] = matrix[i + k, j + l]

            # Check if the sum of all elements in the current submatrix is 35
            if np.sum(current_submatrix) == 35:
                # If so, add the current submatrix to the list of found submatrices
                submatrices.append(current_submatrix)

    return submatrices
