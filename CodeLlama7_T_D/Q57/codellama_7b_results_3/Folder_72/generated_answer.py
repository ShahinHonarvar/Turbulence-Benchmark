
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Get the current row of the matrix
        row = matrix[i]

        # Loop over each column of the row
        for j in range(row.size):
            # Get the current element of the row
            element = row[j]

            # Check if the sum of all elements in the submatrix equals 41
            if np.sum(element) == 41:
                # Add the submatrix to the list of submatrices
                submatrices.append(element)

    # Return the list of submatrices
    return submatrices
