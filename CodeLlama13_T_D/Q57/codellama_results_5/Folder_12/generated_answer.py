
import numpy as np
def submatrices_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with a particular sum
    submatrices = []
    
    # Iterate over each submatrix of the given matrix
    for i in range(matrix.shape[0] - 1):
        for j in range(matrix.shape[1] - 1):
            # Calculate the sum of all integers in the current submatrix
            curr_sum = np.sum(matrix[i:i+2, j:j+2])
            
            # If the current submatrix has a particular sum, add it to the list of submatrices
            if curr_sum == -83:
                submatrices.append(matrix[i:i+2, j:j+2])
    
    return submatrices
