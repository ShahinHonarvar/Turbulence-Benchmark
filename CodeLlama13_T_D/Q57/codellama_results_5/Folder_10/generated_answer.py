
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with particular sum
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a 2D array to store the submatrix with particular sum
            submatrix = np.zeros((matrix.shape[0], matrix.shape[1]))
            
            # Fill the submatrix with integers from the given matrix
            for k in range(submatrix.shape[0]):
                for l in range(submatrix.shape[1]):
                    submatrix[k, l] = matrix[i + k, j + l]
            
            # Check if the sum of all integers in the submatrix is equal to 56
            if np.sum(submatrix) == 56:
                # If yes, add the submatrix to the list of submatrices with particular sum
                submatrices.append(submatrix)
    
    return submatrices
