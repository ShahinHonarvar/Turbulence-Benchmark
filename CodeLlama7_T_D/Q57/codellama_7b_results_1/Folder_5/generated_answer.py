
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a new submatrix with the same dimensions as the original matrix
            submatrix = np.empty((matrix.shape[0] - 1, matrix.shape[1] - 1), dtype=int)
            # Fill the submatrix with the appropriate values from the original matrix
            for m in range(submatrix.shape[0]):
                for n in range(submatrix.shape[1]):
                    submatrix[m, n] = matrix[i + m, j + n]
            # Check if the sum of all integers in the submatrix equals -43
            if np.sum(submatrix) == -43:
                # If so, append the submatrix to the list of submatrices
                submatrices.append(submatrix)
    # Return the list of submatrices that satisfy the given condition
    return submatrices
