
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Get the current row of the matrix
        row = matrix[i]
        # Iterate over each column of the row
        for j in range(row.size):
            # Get the current element of the row and column
            element = row[j]
            # Check if the sum of all integers in the submatrix equals 16
            if np.sum(element) == 16:
                # Add the submatrix to the list of submatrices
                submatrices.append(element)
    # Return the list of submatrices that have a sum of all integers equal to 16
    return submatrices
