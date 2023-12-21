
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each submatrix of the given matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    # Check if the sum of all integers in each submatrix is equal to -43
                    if np.sum(matrix[i:k+1, j:l+1]) == -43:
                        # If a match is found, add the submatrix to the result list
                        result.append(matrix[i:k+1, j:l+1])
    
    # Return the result list
    return result
