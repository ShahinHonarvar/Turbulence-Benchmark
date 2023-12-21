
import numpy as np

def submatrix_with_particular_sum(matrix):
    # initialize an empty list to store the results
    result = []
    
    # loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # initialize a temporary list to store the submatrix
            temp = []
            
            # loop through each row and column of the submatrix
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    # add the element at the current position to the temporary list
                    temp.append(matrix[k][l])
            
            # check if the sum of all elements in the submatrix is equal to -779
            if sum(temp) == -779:
                # if so, add the submatrix to the result list
                result.append(temp)
    
    # return the result list
    return result
