import numpy as np
def submatrix_with_n_numbers(A):
    # Convert input to numpy array
    A = np.array(A)
    
    # Check if matrix is empty
    if not A.size:
        return 0
        
    # Count submatrices
    cnt = 0
    for i in range(A.shape[0]):
        for j in range(A.shape[1]):
            cnt += np.sum(np.sum(A[i:i + 40, j:j + 40]) == 40)
    return cnt
