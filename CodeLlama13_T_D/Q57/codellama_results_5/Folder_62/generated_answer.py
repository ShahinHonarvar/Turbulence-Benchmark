
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the submatrices with sum 394
    submatrices = []
    
    # Iterate over each row of the matrix
    for i in range(matrix.shape[0]):
        # Iterate over each column of the matrix
        for j in range(matrix.shape[1]):
            # Initialize a 2D numpy array to store the current submatrix
            curr_submatrix = np.zeros((matrix.shape[0], matrix.shape[1]), dtype=np.int64)
            
            # Iterate over each element of the current submatrix
            for k in range(curr_submatrix.shape[0]):
                for l in range(curr_submatrix.shape[1]):
                    # Check if the current element is within the bounds of the matrix
                    if i+k < matrix.shape[0] and j+l < matrix.shape[1]:
                        # Add the element to the current submatrix
                        curr_submatrix[k, l] = matrix[i+k, j+l]
                    
            # Check if the sum of all elements in the current submatrix is equal to 394
            if np.sum(curr_submatrix) == 394:
                # Add the current submatrix to the list of submatrices with sum 394
                submatrices.append(curr_submatrix)
    
    return submatrices
