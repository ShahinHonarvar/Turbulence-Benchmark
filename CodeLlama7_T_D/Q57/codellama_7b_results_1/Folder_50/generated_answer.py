
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices
    submatrices = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Get the ith row of the matrix as a 1D array
        row = matrix[i]

        # Loop through each column of the row
        for j in range(row.size):
            # Get the jth element of the row
            element = row[j]

            # If the element is equal to 95, add the submatrix to the list of submatrices
            if element == 95:
                submatrices.append(matrix[i:i+1, j:j+1])

    # Return the list of submatrices that have a sum of all integers equal to 95
    return submatrices
