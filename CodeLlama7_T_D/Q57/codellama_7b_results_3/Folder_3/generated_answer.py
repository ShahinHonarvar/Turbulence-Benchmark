
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the submatrix
            submatrix_sum = 0

            # Loop over each element of the submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Add the element to the submatrix sum
                    submatrix_sum += matrix[row][col]

                    # Check if the submatrix sum equals 54
                    if submatrix_sum == 54:
                        # Append the submatrix to the list of submatrices
                        submatrices.append(matrix[i:i + 3, j:j + 3])

                        # Break out of the inner loop
                        break

    # Return the list of submatrices
    return submatrices
