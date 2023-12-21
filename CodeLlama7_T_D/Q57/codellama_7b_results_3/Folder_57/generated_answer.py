
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the elements in the submatrix
            sum = 0
            # Loop through each element in the submatrix
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    # Add the element to the sum if it is within the bounds of the matrix
                    if k < matrix.shape[0] and l < matrix.shape[1]:
                        sum += matrix[k][l]
            # If the sum equals 13, add the submatrix to the list of submatrices
            if sum == 13:
                submatrices.append(matrix[i:i + 3, j:j + 3])
    # Return the list of submatrices
    return submatrices
