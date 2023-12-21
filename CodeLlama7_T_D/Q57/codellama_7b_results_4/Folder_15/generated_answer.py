
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize the list of all submatrices
    submatrices = []

    # Loop through each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Create a copy of the original matrix
            submatrix = matrix.copy()

            # Remove rows and columns from the copy that do not contain the desired sum
            while True:
                if np.sum(submatrix[i]) == -9 or np.sum(submatrix[:, j]) == -9:
                    submatrix = submatrix[:i] + submatrix[i+1:]
                    submatrix = submatrix[:, :j] + submatrix[:, j+1:]
                else:
                    break

            # Check if the submatrix contains the desired sum and add it to the list if so
            if np.sum(submatrix) == -9:
                submatrices.append(submatrix)

    # Return the list of all submatrices that contain the desired sum
    return submatrices
