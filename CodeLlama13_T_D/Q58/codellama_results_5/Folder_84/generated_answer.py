
import numpy as np
def submatrix_with_n_numbers(matrix):
    # Initialize a counter for the number of submatrices with 127 integers
    count = 0

    # Iterate over each row and column in the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Check if the current element is 127
            if matrix[i][j] == 127:
                # If it is, increment the counter and check the submatrices around it
                count += 1
                for k in range(max(i-1, 0), min(i+2, len(matrix))):
                    for l in range(max(j-1, 0), min(j+2, len(matrix[k]))):
                        # If the submatrices around it contain 127 integers, increment the counter
                        if matrix[k][l] == 127:
                            count += 1
    return count
