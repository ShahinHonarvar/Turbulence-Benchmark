
import numpy as np

def submatrix_with_particular_sum(matrix):
    """
    Returns a list of all submatrices of the given matrix such that the sum of
    all integers in each submatrix equals -86. If no such submatrix is found,
    returns an empty list.
    """
    # Convert the input matrix to a numpy array
    matrix = np.array(matrix)
    
    # Initialize an empty list to store the submatrices with the required sum
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a 2D array to store the current submatrix
            curr_submatrix = np.zeros((matrix.shape[0], matrix.shape[1]), dtype=int)
            
            # Fill the current submatrix with the values from the input matrix
            for k in range(curr_submatrix.shape[0]):
                for l in range(curr_submatrix.shape[1]):
                    curr_submatrix[k, l] = matrix[i + k, j + l]
            
            # Check if the sum of all integers in the current submatrix equals -86
            if np.sum(curr_submatrix) == -86:
                # If yes, add the current submatrix to the list of submatrices with the required sum
                submatrices.append(curr_submatrix)
    
    return submatrices
