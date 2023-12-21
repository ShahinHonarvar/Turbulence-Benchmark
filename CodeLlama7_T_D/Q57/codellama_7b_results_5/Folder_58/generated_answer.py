
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices
    submatrices = []

    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):

        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):

            # Initialize a variable to store the sum of the submatrix
            submatrix_sum = 0

            # Loop over each element of the submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    if row < matrix.shape[0] and col < matrix.shape[1]:
                        submatrix_sum += matrix[row][col]

                    else:

                        # If the element is outside the bounds of the matrix, break from the inner loop
                        break

                if submatrix_sum == -137:
                    # If the sum of the submatrix equals -137, add it to the list of submatrices and break from the outer loop
                    submatrices.append(matrix[i:i + 3][j:j + 3]])
                    break

            if submatrix_sum == -137:
                # If the sum of the submatrix equals -137, add it to the list of submatrices and break from the outer loop
                submatrices.append(matrix[i:i + 3][j:j + 3]])
                break

    return submatrices
