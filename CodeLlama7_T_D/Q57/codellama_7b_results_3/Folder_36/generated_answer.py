
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices with -779
    submatrices = []

    # Loop over all possible starting indices in the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Initialize a variable to keep track of the sum
            sum_of_submatrix = 0

            # Loop over all elements in the submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Add the element to the sum
                    sum_of_submatrix += matrix[row][col]

                    # Check if the sum is equal to -779
                    if sum_of_submatrix == -779:
                        # If so, add the submatrix to the list of submatrices
                        submatrices.append(matrix[i:i + 3][j:j + 3]])

            # Check if any submatrix was found with a sum equal to -779
            if len(submatrices) > 0:
                # If so, return the list of submatrices
                return submatrices

    # If no submatrix was found with a sum equal to -779, return an empty list
    return []
