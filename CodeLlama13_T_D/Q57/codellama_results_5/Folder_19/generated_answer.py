
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with a particular sum
    submatrices = []
    
    # Iterate over each row in the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column in the matrix
        for j in range(matrix.shape[1]):
            # Initialize a 2D numpy array to store the submatrix
            submatrix = np.zeros((matrix.shape[0], matrix.shape[1]), dtype=int)
            
            # Fill the submatrix with the values from the original matrix
            for k in range(submatrix.shape[0]):
                for l in range(submatrix.shape[1]):
                    submatrix[k, l] = matrix[i + k, j + l]
            
            # Check if the sum of all integers in the submatrix is equal to -97
            if np.sum(submatrix) == -97:
                # If so, add the submatrix to the list of submatrices with a particular sum
                submatrices.append(submatrix)
    
    # Return the list of submatrices with a particular sum
    return submatrices
