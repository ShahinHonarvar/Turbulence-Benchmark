
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the elements in the submatrix
            submatrix_sum = 0

            # Loop through each element of the submatrix
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    # Check if the element is within the boundaries of the matrix
                    if k < matrix.shape[0] and l < matrix.shape[1]:
                        # Add the element to the sum of the submatrix
                        submatrix_sum += matrix[k][l]

            # If the sum of the elements in the submatrix is equal to 901, add it to the list of submatrices
            if submatrix_sum == 901:
                submatrices.append(submatrix)

    # Return the list of all submatrices with a sum of 901
    return submatrices
