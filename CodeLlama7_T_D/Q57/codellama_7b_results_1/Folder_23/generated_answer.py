
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices with the sum of all integers in each submatrix equals 59
    submatrices = []
    # Iterate over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Initialize a new submatrix with the sum of all integers in each submatrix equals 59
            submatrix = np.zeros((3, 3))
            # Iterate over each row and column of the submatrix
            for x in range(submatrix.shape[0]):
                for y in range(submatrix.shape[1]):
                    # If the current element is within the boundaries of the original matrix
                    if i + x < matrix.shape[0] and j + y < matrix.shape[1]:
                        # Set the value of the current element in the submatrix to the corresponding value in the original matrix
                        submatrix[x][y] = matrix[i + x][j + y]
            # If the sum of all integers in each submatrix equals 59, add it to the list of submatrices
            if np.sum(submatrix) == 59:
                submatrices.append(submatrix)
    # Return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals 59, or an empty list if no such submatrix is found
    return submatrices
