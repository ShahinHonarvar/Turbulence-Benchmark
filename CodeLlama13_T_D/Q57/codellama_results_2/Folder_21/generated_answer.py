
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    results = []
    
    # Loop through each row of the matrix
    for i in range(len(matrix)):
        # Loop through each column of the matrix
        for j in range(len(matrix[0])):
            # Create a temporary submatrix starting from (i, j)
            temp_submatrix = np.zeros((3, 3), dtype=int)
            
            # Fill the temporary submatrix with integers from the original matrix
            for k in range(3):
                for l in range(3):
                    temp_submatrix[k, l] = matrix[i + k][j + l]
                    
            # Check if the sum of all integers in the temporary submatrix equals -936
            if np.sum(temp_submatrix) == -936:
                # If so, add the temporary submatrix to the results list
                results.append(temp_submatrix)
    
    # Return the results list
    return results
