
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with the particular sum
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a two-dimensional numpy array to store the current submatrix
            current_submatrix = np.zeros((i + 1, j + 1))
            
            # Fill the first row of the current submatrix with the elements from the original matrix
            current_submatrix[0] = matrix[i][j:j+current_submatrix.shape[1]]
            
            # Fill the remaining rows of the current submatrix with the elements from the original matrix
            for k in range(1, current_submatrix.shape[0]):
                current_submatrix[k] = matrix[i + k][j:j+current_submatrix.shape[1]]
            
            # Check if the sum of all integers in the current submatrix is equal to -81
            if np.sum(current_submatrix) == -81:
                # If it is, add the current submatrix to the list of submatrices with the particular sum
                submatrices.append(current_submatrix)
    
    # Return the list of all submatrices with the particular sum
    return submatrices
