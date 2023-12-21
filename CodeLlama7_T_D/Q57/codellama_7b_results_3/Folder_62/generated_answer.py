
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the matrix
        for j in range(len(matrix[i])):
            # Initialize a variable to store the sum of the elements in the submatrix
            sum = 0
            # Loop through each element in the submatrix
            for k in range(len(matrix[i][j])):
                # Add the current element to the sum
                sum += matrix[i][j][k]
            # If the sum of the elements in the submatrix equals 394, add it to the list of submatrices
            if sum == 394:
                submatrices.append(matrix[i][j])
    # Return the list of submatrices that have a sum of 394
    return submatrices
