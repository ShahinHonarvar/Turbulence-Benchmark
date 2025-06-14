
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with sum 830
    submatrices = []
    
    # Loop over each row of the matrix
    for i in range(matrix.shape[0]):
        # Loop over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a 2D numpy array to store the current submatrix
            current_submatrix = np.zeros((matrix.shape[0], matrix.shape[1]), dtype=np.int64)
            
            # Loop over each row of the current submatrix
            for k in range(current_submatrix.shape[0]):
                # Loop over each column of the current submatrix
                for l in range(current_submatrix.shape[1]):
                    # If the current position is within the bounds of the original matrix, add the value to the current submatrix
                    if i + k < matrix.shape[0] and j + l < matrix.shape[1]:
                        current_submatrix[k, l] = matrix[i + k, j + l]
                    
            # If the sum of all integers in the current submatrix is 830, add it to the list of submatrices
            if np.sum(current_submatrix) == 830:
                submatrices.append(current_submatrix)
    
    # Return the list of submatrices with sum 830
    return submatrices
