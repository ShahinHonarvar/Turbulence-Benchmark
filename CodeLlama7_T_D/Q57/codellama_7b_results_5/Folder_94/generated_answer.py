
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Get the current row of the matrix
        row = matrix[i]

        # Iterate over each column of the row
        for j in range(row.size):
            # Get the current element of the row
            element = row[j]

            # Check if the sum of all elements in the submatrix equals 92
            if np.sum(element) == 92:
                # Add the submatrix to the list of submatrices
                submatrices.append(element)

    # Return the list of submatrices that have a sum of 92
    return submatrices
