
import numpy as np
def submatrix_with_particular_sum(matrix):
    # initialize the list of submatrices with sum -44
    submatrices = []
    # loop over all possible combinations of rows and columns
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            # calculate the sum of the current submatrix
            submatrix_sum = matrix[i:j+1].sum()
            # check if the sum is equal to -44
            if submatrix_sum == -44:
                # add the current submatrix to the list of submatrices with sum -44
                submatrices.append(matrix[i:j+1])
    # return the list of all submatrices with sum -44, or an empty list if no such submatrix is found
    return submatrices
