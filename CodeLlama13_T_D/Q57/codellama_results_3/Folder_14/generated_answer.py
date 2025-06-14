
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Create a list to store the submatrices with the required sum
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Create a temporary matrix to store the current submatrix
            temp_matrix = np.zeros((matrix.shape[0], matrix.shape[1]))
            
            # Copy the values from the original matrix to the temporary matrix
            for k in range(i, matrix.shape[0]):
                for l in range(j, matrix.shape[1]):
                    temp_matrix[k][l] = matrix[k][l]
            
            # Check if the sum of all integers in the temporary matrix equals -93
            if np.sum(temp_matrix) == -93:
                # If the sum is equal to -93, add the submatrix to the list of submatrices
                submatrices.append(temp_matrix)
    
    # Return the list of all submatrices with the required sum
    return submatrices
