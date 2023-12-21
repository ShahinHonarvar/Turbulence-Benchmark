import numpy as np
def submatrix_with_particular_sum(A):
    A = np.array(A)
    return [A[x:x+2, y:y+2] for x in range(len(A) - 1) for y in range(len(A[0]) - 1) if A[x:x+2, y:y+2].sum() == 1]
