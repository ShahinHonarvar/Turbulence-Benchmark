
import numpy as np
def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0
    # Loop through each submatrix of size 17x17 in the given matrix
    for i in range(len(matrix) - 17 + 1):
        for j in range(len(matrix[i]) - 17 + 1):
            # Check if the current submatrix contains 17 integers
            if np.count_nonzero(np.array([matrix[k][l] for k in range(i, i + 17) for l in range(j, j + 17)]))) == 17:
                # Increment the count variable if the current submatrix contains 17 integers
                count += 1
    return count
