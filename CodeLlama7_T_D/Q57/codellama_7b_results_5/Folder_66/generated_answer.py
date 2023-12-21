
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices
    submatrices = []
    # Loop over each row and column in the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of elements in the submatrix
            submatrix_sum = 0
            # Loop over each element in the submatrix
            for k in range(i, i + 2):
                for l in range(j, j + 2):
                    # Add the element to the submatrix sum
                    submatrix_sum += matrix[k][l]
            # If the sum of elements in the submatrix is equal to 99, add it to the list of submatrices
            if submatrix_sum == 99:
                submatrices.append(matrix[i:i + 2, j:j + 2])
    # Return the list of submatrices that meet the condition
    return submatrices
