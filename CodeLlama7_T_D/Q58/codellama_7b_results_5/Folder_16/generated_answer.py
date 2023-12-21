
import numpy as np

def submatrix_with_n_numbers(A, n):
    # Initialize the count to 0
    count = 0
    # Iterate over each row and column of A
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            # Check if the current element is equal to n
            if A[i, j] == n:
                # If so, increment the count by 1
                count += 1
    # Return the count of all submatrices that contain n integers each
    return count
