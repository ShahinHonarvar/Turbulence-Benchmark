
import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray, n: int) -> int:
    # Initialize the count to 0
    count = 0
    # Iterate over all possible submatrices of size (n, n)
    for i in range(len(matrix) - n + 1):
        for j in range(len(matrix[i]) - n + 1):
            # Check if the current submatrix contains exactly 107 integers
            if np.count_nonzero(matrix[i:i+n, j:j+n]) == 107:
                # If it does, increment the count
                count += 1

    # Return the count of all submatrices containing exactly 107 integers
    return count
