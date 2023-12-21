
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the elements in the submatrix
            submatrix_sum = 0

            # Loop over each element in the submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Add the element to the sum of the elements in the submatrix
                    submatrix_sum += matrix[row][col]

            # If the sum of the elements in the submatrix is equal to -308, add it to the list of submatrices
            if submatrix_sum == -308:
                submatrices.append(matrix[i:i + 3, j:j + 3])

    # Return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -308
    return submatrices
