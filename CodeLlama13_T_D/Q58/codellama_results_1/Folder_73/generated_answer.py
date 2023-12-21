
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices with 41 integers each
    count = 0
    
    # Iterate over each row and column in the matrix
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            # Check if the current element is equal to 41
            if matrix[i, j] == 41:
                # If it is, check if the submatrix formed by iterating over all elements within a certain distance of this element contains 41 integers each
                for k in range(i - 2, i + 3):
                    for l in range(j - 2, j + 3):
                        # If the submatrix contains 41 integers each, increment the counter
                        if matrix[k, l] == 41:
                            count += 1
    
    # Return the number of submatrices with 41 integers each found in the given matrix
    return count
