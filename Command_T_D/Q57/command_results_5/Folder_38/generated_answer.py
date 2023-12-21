import numpy as np
def submatrix_with_particular_sum(A):
    A = np.array(A)
    return [A[i:j+1][:][:].tolist() for i in range(len(A)-1) for j in range(i+1, len(A))] if A.sum() == 34 else []
