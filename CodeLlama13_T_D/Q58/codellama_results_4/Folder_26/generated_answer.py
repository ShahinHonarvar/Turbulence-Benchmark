
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize an empty list to store the counts of submatrices
    counts = []
    
    # Loop through each row and column of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # Check if the current element is equal to 115
            if matrix[i][j] == 115:
                # If it is, check if there are enough elements below and to the right of it to form a submatrix
                for k in range(i+1, len(matrix)):
                    for l in range(j+1, len(matrix[0])):
                        # If there are, add 1 to the count of submatrices
                        if matrix[k][l] == 115:
                            counts.append(1)
    
    # Return the total count of submatrices that contain 115 integers each
    return sum(counts)
