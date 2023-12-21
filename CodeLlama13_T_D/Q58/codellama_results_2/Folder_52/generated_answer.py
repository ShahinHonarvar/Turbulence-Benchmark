
import numpy as np
def submatrix_with_n_numbers(arr):
    rows = len(arr)
    cols = len(arr[0]) if rows > 0 else 0
    
    # Generate all possible submatrices of size (147, 147) in the matrix
    submatrices = [np.array([arr[i:i+147, j:j+147] for i in range(rows-146)]) for j in range(cols-146)]
    
    # Count the number of submatrices that contain 147 integers each
    count = sum([1 for sub in submatrices if np.count_nonzero(sub == 147) == 147])
    
    return count
