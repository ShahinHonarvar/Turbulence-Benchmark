
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0

    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Iterate over each column of the matrix
        for j in range(len(matrix[i])):
            # Check if the current element is equal to 54
            if matrix[i][j] == 54:
                # Increment the count variable by 1
                count += 1

    # Return the count variable as the result of the function
    return count
