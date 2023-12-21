
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize a list to store the submatrices
    submatrices = []

    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a variable to store the sum of the elements in the submatrix
            submatrix_sum = 0

            # Loop through each element in the submatrix
            for row in range(i, i + 3):
                for col in range(j, j + 3):
                    # Add the current element to the sum of the elements in the submatrix
                    submatrix_sum += matrix[row][col]

                    # If the sum of the elements in the submatrix equals -9, add the submatrix to the list of submatrices and break out of the inner loop
                    if submatrix_sum == -9:
                        submatrices.append(matrix[i:i + 3][j:j + 3]])
                        break

                    # If the sum of the elements in the submatrix does not equal -9, continue looping through the inner loop
                    else:
                        continue

                # If the current element is not a part of a valid submatrix, break out of the outer loop
                if submatrix_sum != -9:
                    break

            # If the current element is a part of a valid submatrix, continue looping through the outer loop
            else:
                continue

        # If the current row or column is not a part of a valid submatrix, break out of the inner loop
        if submatrix_sum != -9:
            break

    # Return the list of all submatrices of the given matrix such that the sum of all integers in each submatrix equals -9. If no such submatrix is found, the function should return an empty list.
    return submatrices
