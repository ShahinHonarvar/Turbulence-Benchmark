
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices
    submatrices = []
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a list to store the elements of the submatrix
            submatrix_elements = []
            # Loop through each row of the submatrix
            for k in range(3):
                # Loop through each column of the submatrix
                for l in range(3):
                    # Add the element at position (k, l) to the list of elements of the submatrix
                    submatrix_elements.append(matrix[i + k][j + l])
            # Check if the sum of all the elements in the submatrix is equal to -336
            if sum(submatrix_elements) == -336:
                # If it is, add the submatrix to the list of submatrices
                submatrices.append(submatrix_elements)
    # Return the list of submatrices that have a sum of all elements equal to -336
    return submatrices
