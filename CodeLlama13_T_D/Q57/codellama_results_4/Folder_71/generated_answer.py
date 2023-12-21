
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with particular sum
    submatrices = []
    
    # Loop through each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop through each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the submatrix
            temp_matrix = np.zeros((matrix.shape[0], matrix.shape[1]), dtype=int)
            
            # Loop through each element of the submatrix
            for k in range(temp_matrix.shape[0]):
                for l in range(temp_matrix.shape[1]):
                    # Check if the element is within the bounds of the matrix
                    if i+k < matrix.shape[0] and j+l < matrix.shape[1]:
                        # Add the element to the temporary matrix
                        temp_matrix[k, l] = matrix[i+k, j+l]
                    
            # Check if the sum of all elements in the temporary matrix is 69
            if np.sum(temp_matrix) == 69:
                # Add the submatrix to the list of submatrices
                submatrices.append(temp_matrix)
    
    # Return the list of submatrices with particular sum
    return submatrices
