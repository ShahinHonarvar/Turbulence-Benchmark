
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Iterate over each column of the matrix
        for j in range(len(matrix[i])):
            # Initialize an empty list to store the elements of the submatrix
            submatrix = []

            # Add the elements of the submatrix to the list
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    submatrix.append(matrix[row][col])

            # Check if the sum of all integers in the submatrix is equal to -157
            if sum(submatrix) == -157:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of submatrices that have a sum of all integers equal to -157
    return submatrices
