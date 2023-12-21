
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over all possible starting rows and columns
    for row in range(matrix.shape[0]):
        for col in range(matrix.shape[1]):
            # Check if the current submatrix has the desired sum
            if np.sum(matrix[row:, col:]) == -63:
                # If it does, add it to the results list
                results.append((row, col))
    
    return results
