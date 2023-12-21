
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop through each row of the matrix
    for i in range(len(matrix)):

        # Loop through each column of the matrix
        for j in range(len(matrix[0])):

            # Initialize an empty list to store the elements of the submatrix
            submatrix = []

            # Add the elements of the submatrix to the list
            for row in range(i, i + 3):
                if row < len(matrix):
                    for col in range(j, j + 3):
                        if col < len(matrix[0]):
                            submatrix.append(matrix[row][col])

            # Check if the sum of the elements in the submatrix is equal to 19
            if sum(submatrix) == 19:

                # Add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # Return the list of all submatrices that have a sum of 19
    return submatrices
