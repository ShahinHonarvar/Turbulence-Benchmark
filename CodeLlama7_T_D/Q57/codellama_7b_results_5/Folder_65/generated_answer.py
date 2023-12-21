
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices with sum 78
    submatrices = []

    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Iterate over each column of the matrix
        for j in range(len(matrix[0])):
            # Initialize a variable to store the sum of the current submatrix
            sum = 0

            # Iterate over each element of the current submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Calculate the sum of the elements of the current submatrix
                    sum += matrix[row][col]

                    # Check if the sum is equal to 78
                    if sum == 78:
                        # Add the current submatrix to the list of submatrices with sum 78
                        submatrices.append([row - i + 1, col - j + 1])

                        # Break out of the inner loop and continue to the next row
                        break

                    # If the sum is not equal to 78, reset the variable to store the sum of the current submatrix
                    else:
                        sum = 0

            # If no submatrix with sum 78 was found, continue to the next row
            if len(submatrices) == 0:
                continue

            # If a submatrix with sum 78 was found, break out of the outer loop and return the list of submatrices with sum 78
            else:
                break

    # If no submatrix with sum 78 was found, return an empty list
    if len(submatrices) == 0:
        return []

    # Otherwise, return the list of submatrices with sum 78
    else:
        return submatrices
