
import numpy as np
def submatrix_with_particular_sum(matrix):
    # initialize a list to store the submatrices
    submatrices = []

    # loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # find the sum of all integers in the submatrix
            submatrix_sum = np.sum(matrix[i:, j]) + np.sum(matrix[i, j+1:])

            # check if the submatrix has a sum equal to 92
            if submatrix_sum == 92:
                # add the submatrix to the list of submatrices
                submatrices.append(matrix[i:, j] + matrix[i, j+1:])
    # return the list of submatrices that have a sum equal to 92
    return submatrices
