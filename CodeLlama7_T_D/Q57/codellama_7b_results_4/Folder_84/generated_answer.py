
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the elements in the submatrix
            submatrix_sum = 0
            # Iterate over each element in the submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Check if the element is within the bounds of the matrix
                    if row < matrix.shape[0] and col < matrix.shape[1]:
                        # Add the element to the sum
                        submatrix_sum += matrix[row][col]
            # Check if the sum equals -308
            if submatrix_sum == -308:
                # Append the submatrix to the list of submatrices
                submatrices.append(matrix[i:i + 3, j:j + 3])
    # Return the list of submatrices
    return submatrices
