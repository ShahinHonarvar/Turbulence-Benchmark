
import numpy as np

def submatrices(A):
    B = np.shape(A)
    for i1 in range(B[0]):
        for j1 in range(B[1]):
            for i2 in range(i1, B[0]):
                for j2 in range(j1, B[1]):
                    yield np.array(A[i1:i2+1, j1:j2+1])

def submatrix_with_particular_sum(matrix):
    result = [submatrix for submatrix in submatrices(matrix) if submatrix.sum() == 27]
    return result
