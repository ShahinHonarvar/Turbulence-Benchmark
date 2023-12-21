
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices with the desired sum
    submatrices = []

    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a list to store the elements of the submatrix
            submatrix = []

            # Iterate from the current row to the last row of the matrix
            for row in range(i, matrix.shape[0]):
                # Iterate from the current column to the last column of the matrix
                for col in range(j, matrix.shape[1]):
                    # Add the element to the submatrix list if it is not already present
                    if (row, col) not in submatrix:
                        submatrix.append((row, col))

            # Check if the sum of all elements in the submatrix equals 126
            if np.sum(np.array([matrix[row, col] for row, col in submatrix])) == 126:
                # Add the submatrix to the list of submatrices with the desired sum
                submatrices.append(submatrix)

    # Return the list of all submatrices with the desired sum
    return submatrices
