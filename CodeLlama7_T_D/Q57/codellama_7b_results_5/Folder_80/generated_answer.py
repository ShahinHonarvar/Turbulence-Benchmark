
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Get the elements of the current row
        row = matrix[i, :]

        # Iterate over each column of the current row
        for j in range(row.size):
            # Get the elements of the current submatrix
            submatrix = np.array([row[:j], row[j:]]))

            # Check if the sum of all integers in the submatrix is equal to 245
            if submatrix.sum() == 245:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices
    return submatrices
