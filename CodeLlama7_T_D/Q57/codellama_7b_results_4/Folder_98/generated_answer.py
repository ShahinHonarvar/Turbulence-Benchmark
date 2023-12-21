
import numpy as np
def submatrix_with_particular_sum(matrix):
    # Initialize the list of submatrices with zero sum
    submatrices = []

    # Iterate over each row and column of the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Calculate the sum of all integers in the submatrix
            sum_submatrix = 0
            for k in range(i, i + 3):
                for l in range(j, j + 3):
                    if k < matrix.shape[0] and l < matrix.shape[1]:
                        sum_submatrix += matrix[k][l]

            # If the sum of all integers in the submatrix is zero, add it to the list of submatrices with zero sum
            if sum_submatrix == 0:
                submatrices.append((i, j))

    # Return the list of submatrices with zero sum
    return submatrices
