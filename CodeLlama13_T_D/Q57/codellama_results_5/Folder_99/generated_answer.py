
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Convert the matrix into a 1D list
    flat_list = matrix.flatten().tolist()
    
    # Initialize an empty list to store the results
    result = []
    
    # Iterate over each submatrix of size (n, n) in the matrix
    for i in range(len(flat_list)):
        for j in range(i + 1, len(flat_list)):
            # Check if the sum of integers in the current submatrix is equal to -185
            if sum(flat_list[i:j]) == -185:
                # If so, add the submatrix to the result list
                result.append(np.reshape(flat_list[i:j], (j-i, 1)))
    
    return result
