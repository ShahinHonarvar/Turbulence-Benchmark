
import numpy as np

def submatrix_with_n_numbers(matrix: np.ndarray, n: int) -> int:
    # Initialize the count variable
    count = 0

    # Iterate over each row of the matrix
    for i in range(len(matrix)):
        # Check if the current row contains the target number
        if matrix[i].sum() == n:
            # Increment the count by 1
            count += 1

    # Return the count of all submatrices that contain the target number
    return count
