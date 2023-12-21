
import numpy as np

def submatrix_with_particular_sum(matrix):
    # initialize an empty list to store the result
    submatrices = []
    
    # loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # calculate the sum of all integers in the submatrix starting from (i, j)
            current_sum = np.sum(matrix[i:, j:])
            
            # if the sum is 398, add the submatrix to the result list
            if current_sum == 398:
                submatrices.append(matrix[i:, j:])
    
    return submatrices
