
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with the particular sum
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a temporary matrix to store the current submatrix
            temp_matrix = np.zeros((matrix.shape[0], matrix.shape[1]), dtype=int)
            
            # Iterate over each row of the temporary matrix
            for k in range(temp_matrix.shape[0]):
                # Iterate over each column of the temporary matrix
                for l in range(temp_matrix.shape[1]):
                    # Set the current element of the temporary matrix to the corresponding element of the original matrix
                    temp_matrix[k, l] = matrix[i + k, j + l]
            
            # Check if the sum of all elements in the temporary matrix is equal to -47
            if np.sum(temp_matrix) == -47:
                # If so, add the temporary matrix to the list of submatrices
                submatrices.append(temp_matrix)
    
    # Return the list of submatrices with the particular sum
    return submatrices
