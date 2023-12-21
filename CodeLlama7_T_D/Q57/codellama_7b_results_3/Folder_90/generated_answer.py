
import numpy as np

def submatrix_with_particular_sum(matrix):
    # initialize an empty list to store the submatrices
    submatrices = []

    # loop through each row of the matrix
    for i in range(matrix.shape[0]):

        # loop through each column of the matrix
        for j in range(matrix.shape[1]):

            # create a copy of the original matrix
            submatrix = np.copy(matrix)

            # remove the current row and column from the submatrix
            submatrix = np.delete(submatrix, i, 0)
            submatrix = np.delete(submatrix, j, 1)

            # check if the sum of all integers in the submatrix is equal to -452
            if np.sum(submatrix) == -452:
                # add the submatrix to the list of submatrices
                submatrices.append(submatrix)

    # return the list of submatrices
    return submatrices
