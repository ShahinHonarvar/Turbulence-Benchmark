
import numpy as np

def submatrix_with_n_numbers(A):
    # Initialize count variable
    count = 0

    # Iterate over all possible submatrices of A
    for i in range(len(A)):
        for j in range(i, len(A[0])):
            # Check if the current submatrix has 46 integers
            if sum(A[i][j]) == 46:
                # Increment count variable
                count += 1

    # Return count variable
    return count
