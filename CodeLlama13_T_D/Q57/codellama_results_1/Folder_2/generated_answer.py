
import numpy as np

def submatrix_with_particular_sum(matrix):
    # Initialize an empty list to store the results
    results = []
    
    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Iterate over each column of the matrix
        for j in range(len(matrix[0])):
            # Initialize a variable to store the sum of integers in the current submatrix
            current_sum = 0
            
            # Iterate over each row and column of the submatrix starting from the current position
            for k in range(i, len(matrix)):
                for l in range(j, len(matrix[0])):
                    # Add the integer at the current position to the sum
                    current_sum += matrix[k][l]
                    
                    # If the current submatrix has a sum of -863, add it to the results list
                    if current_sum == -863:
                        results.append(matrix[i:k+1, j:l+1])
                        
    return results
