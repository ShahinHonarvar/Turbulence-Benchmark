
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices with sum -863
    submatrices = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary sum variable to keep track of the sum of the elements in the submatrix
            temp_sum = 0
            # Loop through each element in the submatrix
            for k in range(i, i + matrix.shape[0]):
                for l in range(j, j + matrix.shape[1])):
                    # Add the element to the temporary sum variable
                    temp_sum += matrix[k][l]
            # If the temporary sum variable is equal to -863, add the submatrix to the list of submatrices with sum -863
            if temp_sum == -863:
                submatrices.append(matrix[i:i + matrix.shape[0], j:j + matrix.shape[1]]))
    # Return the list of submatrices with sum -863
    return submatrices
