
import numpy as np

def submatrix_with_n_numbers(matrix):
    # Initialize the count variable
    count = 0

    # Iterate over all possible submatrices of size nxn
    for i in range(matrix.shape[0] - n + 1):
        for j in range(matrix.shape[1] - n + 1):
            # Check if the current submatrix contains only the target value
            if all([element == target_value for element in matrix[i:i+n, j:j+n]]) and count < 1:
                count += 1

    # Return the count of all submatrices containing the target value
    return count
